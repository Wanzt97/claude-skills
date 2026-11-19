// Vérifie que les valeurs du moteur sont bien celles de la fiche.
// La fiche fait foi : en cas d'écart, corriger lib/cam-search.js.
//   node verifier-jetons.mjs [dossier-du-projet]
// Sans argument : vérifie le gabarit du skill. Avec un dossier : vérifie la copie de ce projet.
import { readFileSync } from "node:fs";
import { join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const skill = fileURLToPath(new URL("..", import.meta.url));
const projet = resolve(process.argv[2] || join(skill, "gabarit"));
const fiche = readFileSync(join(skill, "FICHE.md"), "utf8");
const moteur = readFileSync(join(projet, "lib", "cam-search.js"), "utf8");

const blocFiche = fiche.slice(fiche.indexOf("## 12.")).match(/```json\n([\s\S]*?)```/);
const blocMoteur = moteur.match(/const JETONS = (\{[\s\S]*?\n  \});/);
if (!blocFiche || !blocMoteur) {
  console.error("Bloc de valeurs introuvable dans la fiche ou dans le moteur.");
  process.exit(2);
}
const attendu = JSON.parse(blocFiche[1]);
const reel = new Function(`return ${blocMoteur[1]}`)();

const ecarts = [];
(function comparer(m, f, chemin) {
  for (const [cle, valeur] of Object.entries(m)) {
    const ou = chemin ? `${chemin}.${cle}` : cle;
    if (f == null || !(cle in f)) ecarts.push(`${ou} : absent de la fiche`);
    else if (valeur && typeof valeur === "object" && !Array.isArray(valeur)) comparer(valeur, f[cle], ou);
    else if (JSON.stringify(valeur) !== JSON.stringify(f[cle]))
      ecarts.push(`${ou} : moteur ${JSON.stringify(valeur)}, fiche ${JSON.stringify(f[cle])}`);
  }
})(reel, attendu, "");

if (ecarts.length) {
  console.error(`${ecarts.length} écart(s) entre le moteur et la fiche :\n- ${ecarts.join("\n- ")}`);
  process.exit(1);
}
console.log("Le moteur et la fiche disent la même chose.");
