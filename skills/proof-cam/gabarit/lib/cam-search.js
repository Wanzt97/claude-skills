/*
 * proof-cam — moteur du gabarit.
 *
 * Toutes les durées et courbes viennent de proof-cam/FICHE.md, section 12.
 * Pour changer une valeur : corriger la fiche d'abord, puis recopier ici.
 * Les modèles de scène n'écrivent jamais une durée en dur : ils appellent ces fonctions.
 */
(function () {
  const JETONS = {
    camera: {
      vol_ms: 1240,
      vol_court_ms: 1040,
      vol_long_ms: 1560,
      courbe: [0.6, 0, 0.4, 1],
      derive_pct_par_s: 1.4,
    },
    entrees: {
      fondu_ms: 240,
      fondu_courbe: [0.3, 0.6, 0.3, 0.9],
      mot_fondu_ms: 240,
      calage_apres_le_mot_ms: 100,
      extinction_ms: 320,
      cascade_ms: 200,
      bascule_3d: { de_deg: 90, a_deg: 8, ms: 320 },
      pastille: { de_pct: 50, a_pct: 100, ms: 120 },
      titre_masque: { par_lettre_ms: 200, entre_lettres_ms: 40 },
    },
    compteur: { heros_ms: 1200 },
    surlignage: { ms: 80, entre_deux_ms: 240 },
    visage: { zoom_de: 1.0, zoom_a: 1.044, ancrage_pct: [50, 40] },
  };

  const s = (ms) => ms / 1000;
  const borne = (v) => Math.max(0, Math.min(1, v));

  function bezier(x1, y1, x2, y2) {
    const cx = 3 * x1, bx = 3 * (x2 - x1) - cx, ax = 1 - cx - bx;
    const cy = 3 * y1, by = 3 * (y2 - y1) - cy, ay = 1 - cy - by;
    const X = (t) => ((ax * t + bx) * t + cx) * t;
    const Y = (t) => ((ay * t + by) * t + cy) * t;
    return (p) => {
      if (p <= 0) return 0;
      if (p >= 1) return 1;
      let bas = 0, haut = 1, t = p;
      for (let i = 0; i < 40; i++) {
        if (X(t) < p) bas = t; else haut = t;
        t = (bas + haut) / 2;
      }
      return Y(t);
    };
  }

  const COURBE_VOL = bezier(...JETONS.camera.courbe);
  const COURBE_FONDU = bezier(...JETONS.entrees.fondu_courbe);
  const cubique = (p) => 1 - Math.pow(1 - p, 3); // décélération des compteurs

  const liste = (cible) =>
    typeof cible === "string"
      ? Array.from(document.querySelectorAll(cible))
      : cible instanceof Element ? [cible] : Array.from(cible);
  const un = (cible) => liste(cible)[0];

  function millier(n, decimales) {
    const [entier, frac] = Math.abs(n).toFixed(decimales || 0).split(".");
    const groupe = entier.replace(/\B(?=(\d{3})+(?!\d))/g, " "); // espace fine
    return (n < 0 ? "−" : "") + groupe + (frac ? "," + frac : "");
  }

  /*
   * Une planche : un grand canevas (le « monde ») et une caméra virtuelle.
   *   tl      la timeline GSAP en pause de la sous-composition
   *   monde   l'élément qui contient tout ce qui est posé sur le canevas
   *   duree   la durée de la scène en secondes (= data-duration du host)
   */
  function planche({ tl, monde, duree, largeur = 1920, hauteur = 1080 }) {
    const elMonde = un(monde);
    const vols = [];
    const horloges = [];
    let depart = viser({ x: largeur / 2, y: hauteur / 2 }, 1, 1);

    // Position d'un élément dans le canevas, lue dans la mise en page (pas dans l'image transformée).
    function boite(cible) {
      if (cible && typeof cible.x === "number") return { x: cible.x, y: cible.y, w: cible.w || 0, h: cible.h || 0 };
      const el = un(cible);
      let x = 0, y = 0, n = el;
      while (n && n !== elMonde) { x += n.offsetLeft; y += n.offsetTop; n = n.offsetParent; }
      return { x: x + el.offsetWidth / 2, y: y + el.offsetHeight / 2, w: el.offsetWidth, h: el.offsetHeight };
    }

    // Une scène masquée n'a pas de mise en page : on mesure la cible à la première image
    // où la scène est visible, puis on garde le résultat.
    const mesurable = () => elMonde.offsetWidth > 0;
    function viser(cible, zoom, derive) {
      const v = { cible, zoom, derive, fixe: null };
      v.lire = () => {
        if (v.fixe) return v.fixe;
        const c = v.cible, gauche = c && c.gauche, travers = c && c.travers;
        const b = boite(gauche || travers || c);
        const z = travers ? Math.max(largeur / (b.w || largeur), hauteur / (b.h || hauteur)) * 1.04 : v.zoom;
        const x = gauche ? b.x - b.w / 2 + ((0.5 - c.part) * largeur) / z : b.x;
        const r = { x, y: b.y, s: z, derive: v.derive };
        if (mesurable()) v.fixe = r;
        return r;
      };
      return v;
    }

    function deriver(etat, dt) {
      const k = 1 + (JETONS.camera.derive_pct_par_s / 100) * (etat.derive || 1) * Math.max(0, dt);
      return { x: etat.x, y: etat.y, s: etat.s * k };
    }

    // État de la caméra à l'instant t, recalculé depuis zéro : exact quel que soit l'ordre des images.
    function cameraA(t) {
      let etat = depart.lire(), depuis = 0;
      for (const v of vols) {
        if (t < v.t) break;
        const de = deriver(etat, v.t - depuis), vers = v.vers.lire();
        if (t < v.t + v.d) {
          const p = COURBE_VOL((t - v.t) / v.d);
          return {
            x: de.x + (vers.x - de.x) * p,
            y: de.y + (vers.y - de.y) * p,
            s: de.s * Math.pow(vers.s / de.s, p), // la courbe porte sur le logarithme du zoom
          };
        }
        etat = vers; depuis = v.t + v.d;
      }
      return deriver(etat, t - depuis);
    }

    function appliquer(t) {
      const c = cameraA(t);
      elMonde.style.transform =
        `translate(${largeur / 2 - c.x * c.s}px, ${hauteur / 2 - c.y * c.s}px) scale(${c.s})`;
      for (const f of horloges) f(t);
    }

    const duree_vol = (d) =>
      d === "court" ? s(JETONS.camera.vol_court_ms)
      : d === "long" ? s(JETONS.camera.vol_long_ms)
      : typeof d === "number" ? d : s(JETONS.camera.vol_ms);

    const p = {
      tl,
      jetons: JETONS,

      /** Décale un instant de voix : un élément apparaît 100 ms après le début de son mot. */
      auMot: (t) => t + s(JETONS.entrees.calage_apres_le_mot_ms),

      /**
       * Point à viser pour qu'un texte héros soit ancré à gauche : son bord gauche tombe
       * à 24 % de la largeur du cadre, jamais au centre.
       */
      aGauche: (cible, part = 0.24) => ({ gauche: cible, part }),

      /** Cadrage de la première image. derive : 1 = dérive vers l'avant, -1 = vers l'arrière. */
      cadrer(cible, zoom = 1, derive = 1) {
        depart = viser(cible, zoom, derive);
        return p;
      },

      /** Vol de caméra vers une cible. Renvoie l'instant où la caméra se pose. */
      voler(t, cible, zoom = 1, { duree: d, derive = 1 } = {}) {
        const dv = duree_vol(d);
        vols.push({ t, d: dv, vers: viser(cible, zoom, derive) });
        vols.sort((a, c) => a.t - c.t);
        return t + dv;
      },

      /** Zoom à travers : la cible finit par remplir l'écran. À placer juste avant la fin de la scène. */
      traverser(t, cible, d = 1.4) {
        return p.voler(t, { travers: cible }, 1, { duree: d });
      },

      /** Entrée standard : fondu sur place. */
      apparaitre(cible, t) {
        tl.fromTo(liste(cible), { opacity: 0 }, { opacity: 1, duration: s(JETONS.entrees.fondu_ms), ease: COURBE_FONDU }, t);
        return p;
      },

      /** Vignette vidéo : visible d'un coup. */
      surgir(cible, t) {
        tl.fromTo(liste(cible), { opacity: 0 }, { opacity: 1, duration: 0.001, ease: "none" }, t);
        return p;
      },

      /** Cascade décorative. Pour une énumération dite à voix haute, appeler apparaitre() mot par mot. */
      cascade(cible, t, pas = s(JETONS.entrees.cascade_ms)) {
        liste(cible).forEach((el, i) => p.apparaitre(el, t + i * pas));
        return p;
      },

      /** Focus par extinction : l'élément quitté passe en gris. */
      eteindre(cible, t, opacite = 0.28) {
        tl.to(liste(cible), { opacity: opacite, filter: "grayscale(1)", duration: s(JETONS.entrees.extinction_ms), ease: "none" }, t);
        return p;
      },

      /** Extrait précédent : il perd sa couleur mais reste lisible. */
      desaturer(cible, t) {
        tl.to(liste(cible), { filter: "grayscale(1) contrast(1.15)", duration: s(JETONS.entrees.extinction_ms), ease: "none" }, t);
        return p;
      },

      /** Passe un élément à la couleur d'accent : c'est lui qu'il faut regarder. */
      accentuer(cible, t) {
        const css = getComputedStyle(document.documentElement);
        tl.to(liste(cible), {
          backgroundColor: css.getPropertyValue("--cs-accent").trim(),
          color: css.getPropertyValue("--cs-sur-accent").trim(),
          duration: s(JETONS.entrees.pastille.ms), ease: "none",
        }, t);
        return p;
      },

      /** Texte tapé au clavier dans une maquette d'interface. cps = caractères par seconde. */
      taper(cible, texte, t, cps = 22) {
        const el = un(cible);
        horloges.push((temps) => { el.textContent = texte.slice(0, Math.max(0, Math.floor((temps - t) * cps))); });
        el.textContent = "";
        return t + texte.length / cps;
      },

      /** Barre qui se remplit de gauche à droite (progression, jauge). */
      barre(cible, t, d = 1.2) {
        tl.fromTo(liste(cible), { scaleX: 0 }, { scaleX: 1, transformOrigin: "0% 50%", duration: d, ease: "none" }, t);
        return t + d;
      },

      /**
       * Texte mot à mot. `temps` = début de chaque mot dans la voix (secondes locales à la scène).
       * Le texte de l'élément est découpé en mots ; le calage de 100 ms est ajouté ici.
       */
      motAMot(cible, temps) {
        const el = un(cible);
        const mots = el.textContent.trim().split(/\s+/);
        el.textContent = "";
        mots.forEach((mot, i) => {
          const span = document.createElement("span");
          span.className = "cs-mot";
          span.textContent = mot;
          el.appendChild(span);
          if (i < mots.length - 1) el.appendChild(document.createTextNode(" "));
          const t = temps[Math.min(i, temps.length - 1)];
          tl.fromTo(span, { opacity: 0 }, { opacity: 1, duration: s(JETONS.entrees.mot_fondu_ms), ease: COURBE_FONDU }, p.auMot(t));
        });
        if (temps.length !== mots.length) console.warn(`proof-cam : ${mots.length} mots mais ${temps.length} temps pour`, el.id);
        return p;
      },

      /** Titre masqué : les lettres montent de sous la ligne de base. Réservé aux concepts centraux. */
      titreMasque(cible, t) {
        const el = un(cible);
        const lettres = Array.from(el.textContent);
        el.textContent = "";
        el.classList.add("cs-masque");
        lettres.forEach((lettre, i) => {
          const span = document.createElement("span");
          span.textContent = lettre === " " ? " " : lettre;
          el.appendChild(span);
          tl.fromTo(span, { yPercent: 110 }, {
            yPercent: 0, duration: s(JETONS.entrees.titre_masque.par_lettre_ms), ease: "power2.out",
          }, t + i * s(JETONS.entrees.titre_masque.entre_lettres_ms));
        });
        return p;
      },

      /**
       * Compteur. Il s'arrête à la fin du nombre prononcé : passer `fin` (fin du nombre dans la voix)
       * ou laisser la durée par défaut d'un chiffre héros.
       */
      compteur(cible, { de = 0, a, t, fin, duree: d, decimales = 0, avant = "", apres = "" }) {
        const el = un(cible);
        const dv = fin ? fin - t : d || s(JETONS.compteur.heros_ms);
        const ecrire = (v) => { el.textContent = avant + millier(v, decimales) + apres; };
        horloges.push((temps) => ecrire(de + (a - de) * cubique(borne((temps - t) / dv))));
        ecrire(de);
        p.apparaitre(el, t);
        return t + dv;
      },

      /** Surlignage : à lancer à l'instant où le vol se pose (valeur renvoyée par voler()). */
      surligner(cible, t) {
        liste(cible).forEach((el, i) => {
          tl.fromTo(el, { scaleX: 0 }, {
            scaleX: 1, transformOrigin: "0% 50%", duration: s(JETONS.surlignage.ms), ease: "none",
          }, t + i * s(JETONS.surlignage.entre_deux_ms));
        });
        return p;
      },

      /** Carte qui bascule en 3D et reste légèrement inclinée. */
      basculer(cible, t) {
        const b = JETONS.entrees.bascule_3d;
        tl.fromTo(liste(cible), { opacity: 0, rotationY: b.de_deg, transformPerspective: 1600 }, {
          opacity: 1, rotationY: b.a_deg, transformPerspective: 1600, duration: s(b.ms), ease: "power2.out",
        }, t);
        return p;
      },

      /** Pastille ou point de frise. */
      pastille(cible, t) {
        const b = JETONS.entrees.pastille;
        tl.fromTo(liste(cible), { opacity: 0, scale: b.de_pct / 100 }, {
          opacity: 1, scale: b.a_pct / 100, duration: s(b.ms), ease: "power2.out",
        }, t);
        return p;
      },

      /** Fonction libre recalculée à chaque image à partir du temps de la scène. */
      aChaqueImage(f) { horloges.push(f); return p; },

      /** À appeler en dernier. Branche la caméra et renvoie la timeline à enregistrer. */
      terminer() {
        const horloge = { t: 0 };
        tl.to(horloge, { t: duree, duration: duree, ease: "none", onUpdate: () => appliquer(horloge.t) }, 0);
        appliquer(0);
        return tl;
      },
    };
    return p;
  }

  /**
   * Zoom du visage : avant, lent, linéaire, de 100 à 104,4 % sur chaque bloc.
   * Il repart de 100 % à chaque retour et traverse les jump cuts.
   *   blocs   [[debut, fin], ...] en secondes de montage
   */
  function visage(tl, cible, blocs) {
    const v = JETONS.visage;
    blocs.forEach(([debut, fin]) => {
      tl.fromTo(cible, { scale: v.zoom_de }, {
        scale: v.zoom_a, transformOrigin: `${v.ancrage_pct[0]}% ${v.ancrage_pct[1]}%`,
        duration: fin - debut, ease: "none",
      }, debut);
    });
  }

  /**
   * Attend les trois polices de l'habillage : la position des cibles dépend de la largeur réelle
   * des textes, et une police utilisée seulement dans une scène masquée ne se charge pas toute seule.
   */
  const POLICES = ['800 100px "CS Gras"', '400 40px "CS Mono"', 'italic 400 100px "CS Chute"'];
  const pret = (construire) =>
    Promise.all(POLICES.map((f) => document.fonts.load(f))).then(() => document.fonts.ready).then(construire);

  /** Démo seulement : des temps réguliers. Dans un vrai montage, les temps viennent de transcript.json. */
  const cadence = (t0, n, pas) => Array.from({ length: n }, (_, i) => +(t0 + i * pas).toFixed(3));

  /** Texte sur le visage : mêmes fondus que sur une planche, sur la timeline principale. */
  function motsSurVisage(tl, cible, temps) {
    liste(cible).forEach((el, i) => {
      tl.fromTo(el, { opacity: 0 }, {
        opacity: 1, duration: s(JETONS.entrees.mot_fondu_ms), ease: COURBE_FONDU,
      }, temps[Math.min(i, temps.length - 1)] + s(JETONS.entrees.calage_apres_le_mot_ms));
    });
  }

  window.CamSearch = { JETONS, planche, visage, motsSurVisage, pret, cadence, bezier, COURBE_VOL, COURBE_FONDU, millier };
})();
