// Calcule les indicateurs de rythme d'un storyboard et les compare aux tolérances de la fiche
// (FICHE.md, sections 9 et 12). À lancer après le plan, puis après toute retouche.
//   node controle-plan.mjs chemin/vers/storyboard.json
import { readFileSync } from "node:fs";

const chemin = process.argv[2];
if (!chemin) {
  console.error("Usage : node controle-plan.mjs chemin/vers/storyboard.json");
  process.exit(2);
}
const fiche = readFileSync(new URL("../FICHE.md", import.meta.url), "utf8");
const bloc = fiche.slice(fiche.indexOf("## 12.")).match(/```json\n([\s\S]*?)```/);
const { controle: tol } = JSON.parse(bloc[1]);

const { scenes } = JSON.parse(readFileSync(chemin, "utf8"));
const duree = (s) => s.end - s.start;
const total = Math.max(...scenes.map((s) => s.end));
const visages = scenes.filter((s) => s.type === "visage").sort((a, b) => a.start - b.start);
const animations = scenes.filter((s) => s.type === "animation");

const somme = (l) => l.reduce((n, s) => n + duree(s), 0);
const mediane = (l) => { const t = [...l].sort((a, b) => a - b); return t.length ? t[Math.floor(t.length / 2)] : 0; };

// Plus longue période sans visage, début et fin de vidéo compris.
let absence = 0, fin = 0;
for (const v of visages) { absence = Math.max(absence, v.start - fin); fin = Math.max(fin, v.end); }
absence = Math.max(absence, total - fin);

const beats = animations.reduce((n, s) => n + (s.beats ? s.beats.length : 0), 0);
const lignes = [
  ["Part du visage", somme(visages) / total, tol.part_visage, (v) => `${Math.round(v * 100)} %`],
  ["Part de l'animation", somme(animations) / total, tol.part_animation, (v) => `${Math.round(v * 100)} %`],
  ["Plus longue absence du visage", absence, [0, tol.absence_visage_max_s], (v) => `${v.toFixed(1)} s`],
  ["Durée médiane d'un bloc visage", mediane(visages.map(duree)), tol.bloc_visage_median_s, (v) => `${v.toFixed(1)} s`],
  ["Une animation toutes les", beats ? somme(animations) / beats : Infinity, tol.intervalle_entre_animations_s, (v) => `${v.toFixed(1)} s`],
];

let ecarts = 0;
console.log(`${scenes.length} scènes, ${total.toFixed(1)} s, ${visages.length} blocs visage, ${beats} animations\n`);
for (const [nom, valeur, [bas, haut], ecrire] of lignes) {
  const ok = valeur >= bas && valeur <= haut;
  if (!ok) ecarts++;
  console.log(`${ok ? "OK      " : "À REVOIR"}  ${nom.padEnd(32)} ${ecrire(valeur).padStart(8)}   (attendu : ${ecrire(bas)} à ${ecrire(haut)})`);
}

// Types de scène hors de la liste fermée.
const modeles = ["m01-mur-vignettes", "m02-frise-compteur", "m03-piece-a-conviction", "m04-texte", "m05-objet-filaire", "m06-interface"];
const inconnus = animations.filter((s) => !modeles.includes(s.modele));
if (inconnus.length) {
  ecarts++;
  console.log(`\nÀ REVOIR  Scènes sans modèle du gabarit : ${inconnus.map((s) => s.id).join(", ")}`);
}
process.exit(ecarts ? 1 : 0);
