# La structure d’un système d’identification d’EPVs
Dans ce papier, nous allons décrire un système d’identification des expressions polylexicales verbales EPV basé sur la transition. Ce système est une mise en œuvre partielle du système proposé par Contant M et Nivre J qui s’attaque aux tâches d’identification des unités lexicales et d’analyse de dépendance par transition de façon jointe. Le système parent se base, à son tour, sur le système Arc-standard d’analyse de dépendance par transition. 
## Contexte
La mise en œuvre de ce système vient dans le context d’un Shared Task. Cette tâche s’intéresse à identifier les EPVs. Elle propose des ressources linguistiques annotées de vingt langues de plusieurs familles. Cela signifie que le système attendu doit être langue indépendante.
#Expressions verbales polylexicales 
### Définition
Les expressions polylexicales sont celles qui contiennent plusieurs mots et forment une unité sémantique non-compositionnelle. 
### Genres
Nous nous intéressons dans cette tâche aux expressions verbales de sortes suivantes :
**idiomatiques** : Faire le poids
**À verbe support** : Monter une attaque
**Intransitives** : Se raser
**À Particules** : cette sorte n’existe pas en français !
### Obstacles de l’identification
Les obstacles les plus importants sont nombreux : La continuité de l’expression, l’aspect idiomatique, l’hétérogénéité, la variation morphologique, lexicale, et syntaxique et la non/semi-compositionnalité sémantique..
# Système parrain 
Ce système prend comme entrée une phrase constituée d’une séquence de tokens et prédit sa structure de dépendance syntaxique ainsi que ses unités lexicales, y compris les EPs. La structure résultante combine deux sous-ensembles factorisés : (i) un arbre standard représentant les dépendances syntaxiques entre les éléments lexicaux de la phrase et (ii) une forêt d’arbres lexicaux incluant des MWE identifiés dans la phrase. Il convient de noter que chaque MWE est représenté par un arbre de constituants qui permet aux EPs d’être intégrées
## Représentation
Afin d’achever cet objectif, le système présente une nouvelle représentation qui permet aux EPs réguliers et irréguliers d’être adéquatement représentées sans compromettre la représentation syntaxique. Dans cette représentation, chaque unité lexicale, un seul mot ou un EP, est associée à un nœud lexique, qui a des attributs linguistiques tels que la forme de surface, le lemme, la POS et d’autres traits morphologiques. Les nœuds lexicaux correspondant aux EPs sont dits non terminaux, car ils ont d’autres nœuds lexicaux comme enfants, tandis que les nœuds lexicaux correspondants à des mots simples sont terminaux. Certains nœuds lexicaux sont des nœuds syntaxiques, c’est-à-dire des nœuds de l’arbre syntaxique de dépendance. Ces nœuds sont soit des nœuds non terminaux correspondant à des MWE fixes, soit des nœuds terminaux correspondant à des mots n’appartenant pas à une MWE fixe. Les nœuds syntactiques sont reliés dans une structure arborescente par des relations de dépendance binaires et asymétriques pointant d’un nœud avant à un nœud dépendant.

Fig.1 : Exemple de la représentation proposée.
La définition formelle de la représentation considère qu’elle est une quadruple (V, F, N, A) :
V est l’ensemble des nœuds terminaux, correspondant aux tokens x1,..., xn, 
F est un ensemble d’arbres de V, chaque arbre correspond à un EP fixe et la racine représente la POS de la EP,
N est un ensemble de n — arbres de F, chaque arbre correspondant à un EP non fixé et la racine représente la POS de la EP, 
A est un ensemble d’arcs de dépendance libellés définissant un arbre de F.
Dans l’exemple de l’image, au dessus, ces ensembles ont les composants suivants : 

V={1,2, 3,4, 5,6, 7,8} 

F={1,2, 3,4, A (5,6), 7,8} 

N={1, N (2,3), V (4,8), A (5,6), 7} 

A={(3, det, 1), (3, mod, 2), (4, subj, 3), (4, obj, 8), (8, mod, A [5,6]), (8, mod, 7)}

Où les mots sont numérotés de 1, qui représente le token « Le », jusqu’à 8, qui représente le token « Decisions », et les lettres représentent les étiquettes de POS : « A » pour adverbe, « V » pour verbe, « N » pour nom..
Enfin, il convient de noter que d’une part, cette représentation ne peut représenter que des EPs superposées si elles sont des cas d’encastrement et que le système d’analyse syntaxique ne réussit pas à parser les EPs superposées des cas d’entrelacement qui sont bien présentés. D’autre part, la binarisation des arbres obtenus est recommandée pour s’adapter à la procédure de l’analyse syntaxique bin que es nœuds temporaires intermédiaires obtenus lors de cette binarisation ne sont utilisés que pour le traitement interne.
## Modèle à base de transition
Le système, que Constant M. et Navire J. ont proposé, est une extension légère d’une analyse de dépendance d’Arc-standard, intégrant des transitions spécifiques pour l’identification des EPs. Ce système utilise deux piles au lieu d’une dans l’objectif de traiter les deux tâches séparément. La synchronisation de ces deux piles est appliquée en utilisant un seul buffer. Il inclut également différentes contraintes destinées à réduire les ambiguïtés créées artificiellement à cause de nouvelles transitions.
### Définition formelle
Le système de transition est un quadruplet S = (C, T, cs, Ct) où : 

1.C est un ensemble de configurations, 

2.T est un ensemble de transitions, dont chacune est partielle Function t : C → C, 

3.cs est une fonction d’initialisation qui mappe chaque phrase d’entréex à une configuration initiale.

Ct ⊆ C est un ensemble de configurations terminales.
Une suite de transitions pour une phrase x est une suite de configurations C0, m = c0,..., cm tel que c0 = cs (x), cm∈Ct, et pour tout ci : (0≤i <m), il existe t∈T tel que t (ci) = ci+1.
L’entraînement de tel système signifie l’entraînement du modèle pour classer les séquences de transition potentielles. Cela nécessite un oracle qui détermine quelle est une séquence de transition optimale donnée une phrase d’entrée et la représentation de sortie correcte. Les oracles statiques définissent une unique séquence de transition unique pour chaque paire entrée-sortie. Les oracles dynamiques permettent plus d’une séquence de transition optimal. Une fois qu’un modèle de notation a été entraîné, l’analyse est généralement effectuée en utilisant des algorithmes de la recherche best-first sous ce modèle.
### Analyse des dépendances Arc-Standard 
Une configuration dans ce système est un triple c = (σ, β, A), où σ est une pile contenant des nœuds partiellement traités, β est un buffer contenant des nœuds d’entrée restants, et A est un ensemble d’arcs de dépendance. La configuration initiale correspond à x = x1,..., xn cs (x) = ([], [1,..., n], {}) et l’ensemble Ct des configurations terminales contient toute configuration de la forme c= ([i], [], A). L’arbre de dépendance défini par une telle configuration de terminal est ({1,..., n}, A). Il existe trois transitions possibles :
Shift : prend le premier nœud dans le tampon et le pousse sur la pile. 
Right-Arc (k) : ajoute un arc de dépendance (i, k, j) à A, où j est le premier et i est le second élément de la pile, et supprime j de la pile.
Left-Arc (k) : ajoute un arc de dépendance (j, k, i) à A, où j est le premier et i est le second élément de la pile, et supprime i de la pile.
###Analyse syntaxique et lexicale conjointe
Ce système produit une structure de deux dimensions parallèles : la dimension syntaxique, représentée par un arbre de dépendance, et la dimension lexicale, représentée par une forêt d’arbres (binaires) d’EPs.
La configuration de cet analyseur utilise deux piles, une pour chaque dimension, et un seul buffer. En outre, nous nous servons de l’ensemble d’arcs de dépendance du système précédent, et d’un autre ensemble dédié aux unités lexicales. 

Fig.2 : La définition formelle du système conjoint
La configuration de ce système se compose donc d’un quintuple c = (σ1, σ2, β, A, L), où σ1 et σ2 sont des piles contenant des nœuds sous-traitement, qui peuvent maintenant être des EPs complexes, β est un buffer contenant des nœuds d’entrée restants, qui sont toujours des tokens, A est un ensemble d’arcs de dépendance, et L est un ensemble d’unités lexicales (tokens ou EPs). La configuration initiale associe la phrase x = x1,..., xn à cs (x) = ([], [], [1,..., n], {}, {}) et l’ensemble Ct des configurations terminales contient tout configuration de la forme c = ([x], [], [], A, L). L’arbre de dépendance défini par une telle configuration terminale est (F, A), et l’ensemble des unités lexicales est V∪L.
Les transitions possibles de ce système sont les suivantes : 
Shift : prend le premier nœud dans le buffer et le pousse sur les deux piles qui garantit la synchronisation des deux tâches au niveau du token. 

**Right-Arc (k)** : le même fonctionnement du système précédent où σ2 ne se change pas.

**Left-Arc (k)** : le même fonctionnement du système précédent où σ2 ne se change pas.

**MergeF (t)** : s’applique dans une configuration où les deux éléments supérieurs x et y sont identiques sur les deux piles et combine ces éléments en un arbre t (x, y) représentant un EP fixe avec un tag de POS. Comme il fonctionne sur les deux piles, le nouvel élément sera un nœud syntaxique ainsi qu’un nœud lexical. 

**MergeN (t)** combine les deux éléments supérieurs x et y dans la pile lexicale σ2 comme un arbre t (x, y) représentant une EP non fixée avec un tag POS. Comme il ne fonctionne que sur la pile lexicale, le nouvel élément ne sera pas un nœud syntaxique.

**Complete** : déplace l’élément supérieur x sur la pile lexicale σ2 à L, ce qui en fait une unité lexicale finale dans la représentation de sortie. Il convient de noter que x peut être un token simple, un EP fixe ou un EP non-fixe.

Fig.3 : Le fonctionnement du système conjoint avec les données d’entrée de Fig.1
### Analyse lexicale simplifiée
Nous allons décrire dans cette section la structure de notre modèle d’identification des EPs. Ce modèle est une version simplifiée du modèle précédent. Les données d’entrée de ce système sont une séquence de tokens qui représente une phrase. Cette séquence doit être traitée par un système à base de transition dans l’objectif d’identifier ses expressions polylexicales verbales. Ce système se base sur le modèle précédent et se limite à la dimension lexicale. Par conséquent, la pile syntaxique est éliminée et les transitions requises ne sont plus si nombreuses.

La configuration de ce système se compose donc d’un triplet c = (σ, β, L), où σ est une pile lexicale contenant des parties des EPVs en train d’être identifiées, β est un buffer contenant des tokens d’entrée restants, et L est un ensemble des EPVs identifiées. 

La configuration initiale associe la phrase x = x1,..., xn à cs (x) = ([], [1,..., n], {}) et l’ensemble Ct des configurations terminales contient toute configuration de la forme c = ([], [], L). À la fin de l’analyse L doit contenir toutes les EPVs identifiées avec un tag indiquant leur type à côté des tokens qui ne font partie d’aucune EPV. (Voir la sous-section intitulée genres de la section Expressions verbales polylexicales).
Les transitions possibles de ce système se limitent aux suivantes : 
**Shift** : prend le premier nœud dans le buffer et le pousse sur la pile. 
**Merge** combine les deux éléments supérieurs x et y dans la pile lexicale σ comme un arbre t (x, y) représentant une EPV avec un tag de genre.
**Complete** : déplace l’élément supérieur x sur la pile lexicale σ à L, ce qui en fait une EPV complète.
Transition
Configuration


([], [1,2, 3,4, 5,6, 7,8], L0= {})
Shift⇒
([1], [2,3, 4,5, 6,7, 8], L0= {})
Complete⇒
([],[2,3, 4,5, 6,7, 8], L0= {1})
Shift⇒
([2], [3,4, 5,6, 7,8], L0= {1})
Complete⇒
([],[3,4, 5,6, 7,8], L0= {1,2})
Shift⇒
([3], [4,5, 6,7, 8], L0= {1,2})
Complete⇒
([],[4,5,6,7,8],L0={1,2,3} )
Shift⇒
([4], [5,6,7,8], L0= {1,2,3})
Shift⇒
([4,5], [6,7, 8], L0= {1,2, 3})
Complete⇒
([4], [6,7,8], L0= {1,2,3,5})
Shift⇒
([4,6], [7,8], L0= {1,2, 3,5})
Complete⇒
([4], [7,8], L0= {1,2, 3,5, 6})
Shift⇒
([4,7], [8], L0= {1,2, 3,5, 6})
Complete⇒
([4], [8], L0= {1,2, 3,5, 6,7})
Shift⇒
([4,8], [], L0= {1,2, 3,5, 6,7})
Merge⇒
([VS [4,8]], [], L0= {1,2, 3,5, 6,7})
Complete⇒
([],[],L0= {1,2, 3,5, 6,7, VS [4,8]})
Fig.4 L’analyse simplifiée de la même phrase précédente.
L’exemple précédent montre la façon du fonctionnement de notre système. L’analyseur arrive à identifier l’EPV « Make decision » qui est la seule EPV dans cette phrase et ajoute le tag VS qui fait le lien à son type : Expression polylexicale à verbe support. D’autre part, l’exemple suivant, qui analyse la phrase : « Let the cat out of the bag », montre un handicap de notre méthode. Elle n’arrive à identifier qu’une seule EPV de la phrase qui en contient deux : le verbe « let out » comme une EPV à particule et la phrase entière comme une EPV idiomatique. La raison de ce handicap revient à la représentation que nous avons proposée et aux transitions que le modèle s’en sert. 
Transition
Configuration


([], [1,2, 3,4, 5,6, 7], L0= {})
Shift⇒
([1], [2,3, 4,5, 6,7], L0= {})
Shift⇒
([1,2], [3,4, 5,6, 7], L0= {})
Shift⇒
([1,2, 3], [4,5, 6,7], L0= {})
Shift⇒
([1,2, 3,4], [5,6, 7], L0= {})
Shift⇒
([1,2, 3,4, 5], [6,7], L0= {})
Shift⇒
([1,2, 3,4, 5,6], [7], L0= {})
Shift⇒
([1,2, 3,4, 5,6, 7], [], L0= {})
Merge⇒
([EPVI [1,2, 3,4, 5,6, 7]], [], L0= {1,2, 3})
Complete⇒
([],[],L0= {EPVI [1,2, 3,4, 5,6, 7]})
Fig.4 L’analyse simplifiée de la phrase : « let : 1 the:2 cat:3 out : 4 of:5 the:6 bag:7 » qui identifie toute la phrase comme EPV idiomatique.
Transition
Configuration


([], [1,2, 3,4, 5,6, 7], L0= {})
Shift⇒
([1], [2,3, 4,5, 6,7], L0= {})
Shift⇒
([1,2], [3,4, 5,6, 7], L0= {})
Complete⇒
([1], [3,4, 5,6, 7], L0= {2})
Shift⇒
([1,3], [4,5, 6,7], L0= {2})
Complete⇒
([1], [4,5, 6,7], L0= {2,3})
Shift⇒
([1,4], [5,6,7], L0= {2,3})
Merge⇒
([EVS(1,4)], [5,6,7], L0= {2,3})
Complete⇒
([],[5,6,7], L0= {2,3, EVS(1,4)})
Shift⇒
[[5], [6,7], L0= {2,3, EVS(1,4)})
Complete⇒
([],[6,7], L0= {2,3, EVS(1,4), 5})
Shift⇒
[[6], [7], L0= {2,3, EVS(1,4), 5})
Complete⇒
([],[7], L0= {2,3, EVS(1,4), 5,6})
Shift⇒
[[7], [], L0= {2,3, EVS(1,4), 5,6})
Complete⇒
([],[],L0= {2,3, EVS(1,4), 5,6, 7})
Fig.4 L’analyse simplifiée de la phrase : “let : 1 the:2 cat:3 out : 4 of:5 the:6 bag:7” qui identifie toute la phrase comme EPV idiomatique.
###Notion pour traiter les cas d’embeding
Dans l’exemple précédent, nous constatons que l’analyse ordinaire ne peut pas traiter les cas d’embeding. Nous proposons donc un algorithme pour appliquer cette analyse de manière itérative en utilisant notre mémoire de la première analyse. Dans cet algorithme nous forçons le classifieur de choisir une autre transition quand il arrive à un des tokens qui forme la première EPV identifiée. 
Appliquer l’analyse simplifiée
Pour chaque EPV de longueur n : 
pos = la position de la tête de la EPV.
Pour idx de 1 à n : 
idx += pos
Appliquer l’analyse simplifiée en évitant le choix classique du classifieur dans la position idx.
Si le classifieur identifie une autre EPV :
break
Dans le cas de la phrase “Let the cat out of the bag”, et à la suite de l’identification de la première EPV idiomatique, la première itération va essayer d’éviter le choix de la transition shift pour la première transition, mais il n’y a pas d’autre transition possible. L’analyseur n’arrive à identifier aucune EPV s’il remplace la deuxième transition, mais il peut identifier la deuxième EPV s’il refuse de choisir la shift pour la troisième transition et la remplace par la transition Complete. 



