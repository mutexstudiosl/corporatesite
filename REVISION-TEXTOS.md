# Revisión de textos (inglés) – mutexstudio.com

Rama: `revision-textos`. Páginas editadas: `index.html`, `azure-autoscaler/`, `storage-observer/`, `traefik-precompiled/`, `consulting/`, `support/`.

## Criterios aplicados

- Solo se ha tocado texto visible, `meta description`, `<title>` (portada) y `aria-label` de gráficos. No se ha cambiado estructura HTML, clases, IDs, enlaces, scripts, CSS ni formularios (incluidos sus *placeholders*).
- No se han tocado: navegación (incluidas las descripciones del desplegable), enlaces del pie, línea legal del pie (razón social, NIF, email), avisos de marca (`trademark-note`, tarjeta "Trademark notice" y el *disclaimer* de Traefik), ni las páginas `aviso-legal/`, `privacy/`, `cookies/`.
- Se han mantenido todas las cifras, precios, nombres de producto, URLs y afirmaciones. Se han revisado los cálculos (ver más abajo) y son coherentes.
- El *tagline* del pie ("Infrastructure tooling that fills the gaps. Self-hosted, production-grade.") **no se ha cambiado**, porque también aparece en las páginas legales y quedaría inconsistente.
- Criterios de estilo:
  - Quitar rayas (—) usadas como muletilla.
  - Quitar relleno de marketing ("intelligently", "engineered from the ground up", "zero babysitting", "landscape", "unified").
  - Pasar los títulos de tarjetas y *eyebrows* a mayúscula solo inicial (*sentence case*), igual que los H2.
  - Unificar términos: "C# lambda expressions", "open-source" en lugar de "OSS", "Azure file shares", "AKS node pools", "elastic pools".
  - Corregir frases fragmentadas o telegráficas.

## Cambios por página

### Portada (`index.html`)

| Antes | Después | Motivo |
|---|---|---|
| `<title>` Infrastructure Tooling That Fills the Gaps | Infrastructure tooling that fills the gaps | Igual que el H1; *sentence case*. |
| meta: "Mutex Studio — Self-hosted infrastructure tooling for…" | "Mutex Studio builds self-hosted infrastructure tools for Azure, Kubernetes, and DevOps, and offers consulting in the same areas." | Frase completa; la consultoría también aparece en la portada. |
| "…built by engineers who ran out of patience with what cloud vendors and generic platforms didn't ship." | "…built by engineers who got tired of waiting for cloud vendors and generic platforms to ship them." | La sintaxis original era enrevesada. |
| "Explore Products and Services" | "See products and services" | Mayúsculas innecesarias; más directo. |
| "Tools we build. Problems we solve." | "Tools for the gaps we kept hitting." | Era un eslogan genérico; ahora conecta con el titular. |
| "Every product fills a real gap — things Azure… should do but don't." | "Each product covers something Azure, Kubernetes, or the cloud vendors should handle and don't." | Sin raya; más natural. |
| Tarjeta Autoscaler: "Automatically scale SQL, MySQL, … File Shares, Elastic Pools, AKS… No more overprovisioning or broken autoscaling." | "Scales Azure SQL databases and elastic pools, … AKS node pools… Stop overprovisioning, and stop relying on built-in autoscaling that breaks in edge cases." | Mayúsculas arbitrarias; términos alineados con la página del producto; "broken autoscaling" se concreta como en la propia página. |
| Tarjeta Storage Observer: "Monitor files and storage across multiple sources at any scale… Azure, S3, NFS, and more — fully self-hosted." | "Shows which folders use your storage across local disks, NFS and SMB shares, SharePoint, S3, and Azure. Built for billions of files, and fully self-hosted." | Dice qué hace realmente el producto; lista de fuentes alineada con su página. |
| "We don't just ship tools — we put them in production. Need help architecting…, taming…, CI/CD pipeline that actually works?" | "We also run these tools in production. If you need help designing Azure infrastructure, getting a Kubernetes cluster under control, or building a CI/CD pipeline that works, we can help." | Menos tono publicitario; sin raya ni "actually". |

### Azure Autoscaler

| Antes | Después | Motivo |
|---|---|---|
| Caption: "A P4 database (500 DTU), left on all month, is €1,606… so the month is €760. List price…" | "A P4 database (500 DTU) left running all month costs €1,606… and the month costs €760. List prices…" | Sintaxis correcta ("is €1,606" → "costs"). |
| "Azure scales some things.<br>Not all things." | "Azure scales some resources.<br>Not all of them." | Más preciso y natural. |
| "Critical PaaS resources on Azure are flexible but don't autoscale. You end up continuously monitoring… Or worse, …simply fail in edge cases." | "Many critical Azure PaaS resources can be resized, but Azure won't resize them for you. Someone has to watch the metrics… Where autoscaling does exist, it can fail in edge cases." | "Flexible" era ambiguo; quitada la dramatización ("Or worse", "simply"). |
| "…containerized solution that monitors your resources and scales them intelligently — based on…" | "It runs as a self-hosted container, watches your resources, and scales them based on real-time metrics, forecasts, or schedules you define." | Quitados "solution" e "intelligently"; sin raya. |
| "Publish the series Azure does not have." + párrafo telegráfico ("Node pool node count. On Azure SQL, …") | "Publish the metrics Azure doesn't have." + "Examples: node count for an AKS node pool, and replica DTU, memory, and replica latency for Azure SQL." | Las frases sin verbo parecían notas sueltas. |
| "Example. The replica series is custom. dtu_used is the platform metric." | "Example data. replica_dtu_used is a custom metric; dtu_used is the platform metric." | Nombra la serie igual que la leyenda. |
| "Lambdas in the rule" / "This one reads…" | "C# lambdas in rules" / "This rule reads…" | Término unificado y referente claro. |
| "Smart scaling, zero babysitting" | "Scaling you don't have to watch" | Sin cliché. |
| Títulos "Self-Hosted", "Schedule-Based Scaling", "Flexible Metric Analysis"… | "Self-hosted", "Schedule-based scaling", "Flexible metric rules"… | *Sentence case*; "rules" describe mejor la tarjeta. |
| "…using Lambda expressions… Total control without code changes." | "…as C# lambda expressions… You get full control without changing the autoscaler's code." | "Lambda" iba en mayúscula; ahora queda claro qué código no hay que cambiar (las reglas sí son código). |
| "…predict future demand and scale proactively — before load spikes cause degraded performance." | "…predict demand and scale ahead of it, before a load spike degrades performance." | Menos relleno. |
| "The system automatically picks…" | "The autoscaler picks…" | Sujeto concreto. |
| "Deploy and forget" / "Deploy the containerized solution, grant permissions…" | "Three steps to production" / "Deploy the container, grant it the permissions it needs…" | El tono "forget" chocaba con el paso 3 ("Monitor and optimize"). |
| "Enable the solution and forget about manually scaling or babysitting your resources ever again." | "Enable it. Nobody has to resize those resources by hand anymore." | Menos hipérbole. |
| Licencias: "You receive access to a private container registry, where you pull container images that are already built, and a license code. Set that code in the environment variables of the deployment." | "You get a license code and access to a private container registry with prebuilt images. Set the license code as an environment variable in your deployment." | Frase más corta y clara (mismo cambio en Storage Observer). |
| "Or only pay for what you save… After that, regular licensing." | "Or pay only for what you save… for the first 12 months our fee is 50%… After that, standard licensing applies." | Orden de "only"; última frase completa. |
| "Ideal for enterprise procurement and MACC." | "A good fit for enterprise procurement and MACC." | Menos superlativo (igual en Storage Observer). |

### Storage Observer

| Antes | Después | Motivo |
|---|---|---|
| "Capacity is one number. The folder that holds it is not." | "Capacity is a single number. It doesn't tell you which folder is using it." | El juego de palabras original no se entendía bien. |
| "Daemons where the files are.<br>One screen for the storage." | "A daemon next to each source.<br>One screen for all your storage." | Más claro. |
| "Deploy a daemon next to each source. It reads… The GUI shows how much each source consumes." | "Each daemon runs next to the storage it scans: … It reports usage to a central server, and the UI shows how much each source uses." | Evita repetir el titular; "GUI" → "UI". |
| Navigation: "…The rest is underneath. Each row splits what sits in this directory — direct files and direct folders — from… Sort by direct children when the size is only being passed through." | "…hold only 12 files; the rest is further down. Each row separates what sits directly in the folder (direct files and direct folders) from the totals for the whole tree… Sort by direct children to skip past folders that only pass the size through." | La última frase era ininteligible. |
| Speed: "Measured while enumerating… SMB metadata latency makes that share a slow source. A local disk or another protocol lists at a different rate." | "Measured while listing an Azure Files share over SMB, where each entry is… SMB metadata latency makes this a slow source; local disks and other protocols list at different rates." | Frases unidas; más fluido. |
| "See everything.<br>Miss nothing." + "…a unified, real-time view of your file and storage landscape…" | "All your storage.<br>One place to look." + "…brings files and storage from any number of sources into one real-time view, without moving your data." | Eslogan genérico y jerga ("landscape", "unified"). |
| "Engineered from the ground up for massive scale…" | "Designed for very large file counts. Performance stays consistent whether a source holds millions of files or billions." | Cliché fuera; se mantiene la afirmación. |
| "Optimization" / "Optimized data refreshing… to reduce IOPS-heavy storage usage." | "Lighter on IOPS" / "Refreshes are tuned to historical usage patterns, which cuts the IOPS spent rescanning storage." | Título vacío y frase sin verbo. |
| "Gain cost visibility into storage spend…" | "See what storage costs across all your accounts and providers" | Jerga. |
| "Compliance and audit trails — know what files exist…" | "Keep an audit trail for compliance: which files exist, where, and since when" | Ahora es paralela al resto de la lista (todas empiezan por verbo). |

### Traefork

| Antes | Después | Motivo |
|---|---|---|
| "…kept in sync with upstream. It precompiles additional plugins into Traefik itself." | "…kept in sync with upstream, with extra plugins compiled into the Traefik binary." | Misma fórmula en portada, meta y hero. |
| "Request Access" | "Request access" | *Sentence case* en botones. |
| "Those middlewares run on every request…" | "That middleware runs on every request…" | "Middleware" es incontable. |
| "The plugin source stays the same. Upstream declined shipping that workflow." | "…without changing the plugin source. Upstream chose not to ship this workflow." | "Declined shipping" no es gramatical. |
| "…are part of the Traefik build. Yaegi does not run them. A Yaegi plugin can still be loaded when it is not in this set." | "…are built into the Traefik binary, so Yaegi doesn't run them. Plugins outside this set can still be loaded through Yaegi." | Frases telegráficas. |
| "The image is exercised with the compiled middlewares…" | "Before an image is published, it is tested with the compiled-in middleware…" | "Exercised" sonaba a traducción. |
| "The request is the advantage." + "You switch because Traefork handles the request…" | "Switch for the request handling, not the bandwidth." + "The reason to move is what Traefork does with each request… Bandwidth costs about the same either way." | El titular no se entendía; se explicita la conclusión que ya dan los precios del párrafo ($0.083 frente a $0.08). |
| "TLS ends at/on…" | "TLS terminates at/on…" | Término técnico habitual. |
| Coste: "Five million requests a day, about 4 KB on the way back. That is 600 GB out. Front Door Premium is $607.80. Traefork is $143.58…" | "Take five million requests a day with responses of about 4 KB. That is 600 GB out per month. Front Door Premium comes to $607.80 and Traefork to $143.58…" | Las frases sueltas y sin verbo costaban de seguir. |
| Tabla: "Month" | "Monthly total" | Etiqueta de la fila de total. |
| Nota: "You keep $464.22… the requests after that are contact-us… this log cannot use the Basic plan…" | "You save $464.22 a month, or $5,571 a year… beyond that, Microsoft quotes the price on request… this log type can't use the Basic plan…" | "Contact-us" como adjetivo era jerga; frases más claras, mismas cifras. |
| "This page summarizes the approach — the authoritative list is…" | "This section summarizes our approach. The authoritative list is…" | Es una sección, no la página entera; sin raya. |
| "OSS" | "open-source" | Término unificado con el resto de la sección. |

### Consulting

| Antes | Después | Motivo |
|---|---|---|
| "…and tame Kubernetes clusters — the same way we do it for our own products." | "…and get Kubernetes clusters under control, the same way we do for our own products." | Sin raya; "do it" sobraba. |
| "Azure SQL, MySQL, Storage architecture" | "Azure SQL, MySQL, and Storage architecture" | Enumeración. |
| "ArgoCD" | "Argo CD" | Nombre oficial del proyecto. |
| "We run the infrastructure — and we've built the tools. …are tools we created because we encountered the same problems…" | "We run infrastructure, and we built our own tools for it. …exist because we kept running into the same problems…" | Repetición de "tools"; sin raya. |
| "When we help you optimize…, or build your CI/CD pipeline — it's based on years of hands-on production experience, not certifications." | "…the advice comes from years of hands-on production work, not from certifications." | La raya rompía la sintaxis; "it's" no tenía referente. |
| "We respond within one business day — usually faster." | "We reply within one business day, usually sooner." | Sin raya. |
| "Serving clients globally" / "Mutex Studio S.L. — a Spanish company…" | "Clients worldwide" / "Mutex Studio S.L. is a Spanish company…" | Frase completa. |

### Support

| Antes | Después | Motivo |
|---|---|---|
| "We're here to<br>help" | "How can we<br>help?" | Fórmula menos manida. |
| "Questions about our products or an existing project? Email us directly…" | "Questions about one of our products or an ongoing project? Email us…" | Más natural. |
| "Write to us at the address below, or use the form. We'll get back to you as soon as we can." | "Email us at the address below or use the form, and we'll reply as soon as we can." | Más conciso. |

## Sugerencias no aplicadas (fuera del alcance permitido)

### Navegación, formularios y script

- **Descripciones del menú "Products"** (no se han tocado por ser navegación):
  - "Smart resource scaling" es genérico. Alternativa: "Scale Azure resources to demand".
  - "File storage at any scale" no dice qué hace el producto. Alternativa: "See which folders use your storage".
- **Formulario de Support**: el *placeholder* "Tell us more about your project" no encaja en una página de soporte. Alternativa: "Describe the issue or question".
- **Teléfono obligatorio** en ambos formularios (`required`). Valorar hacerlo opcional, por fricción y por minimización de datos (RGPD art. 5.1.c).
- **Banner de cookies** (`assets/js/site.js`): "We use Google Analytics cookies to understand how the site is used, only if you accept." tiene un orden poco natural. Propuesta: "With your consent, we use Google Analytics cookies to see how the site is used. If you don't accept, no analytics cookies are set."
- **Comentario en el YAML de ejemplo** (Autoscaler): `# Convert to Gb` debería ser `GB` (está dentro de un bloque de código y no se ha tocado).
- **Pie**: el enlace "Aviso legal" está en español entre etiquetas en inglés. Se puede mantener por exigencia legal española, pero conviene que sea una decisión consciente. Alternativa: "Legal notice (Aviso legal)".

### Páginas legales

**Aviso legal**
- El domicilio "08780 Pallejà (Barcelona)" está incompleto. El art. 10 de la LSSI exige la dirección completa (calle y número). **Es lo más importante de esta lista.**
- En la versión inglesa se mezcla ortografía británica ("licences", "endeavours") con la americana del resto del sitio ("license"). Conviene unificar a la americana.
- "1st inscription" → "first entry"; "sheet B-665521" → "page B-665521".

**Privacy**
- Solo existe en inglés, mientras que el aviso legal es bilingüe. Valorar una versión en español.
- Indicar el mecanismo de transferencia de Google Analytics (por ejemplo, EU-US Data Privacy Framework) y el plazo de conservación concreto configurado en GA.
- Formspree: indicar cuánto tiempo conserva los mensajes.

**Cookies**
- El encabezado "Third-party services you trigger" va seguido solo de "Fonts are served from this site, not from Google.", así que no casa con su contenido. Propuesta: "Other third parties", mencionando que al enviar el formulario los datos van a Formspree.
- "MUTEX STUDIO S.L. uses cookies on this website": sin consentimiento no se instala ninguna cookie (solo `localStorage`). Más exacto: "may use cookies".

## Incoherencias de hechos detectadas (no corregidas)

1. **Enlace de Marketplace de Storage Observer vacío**: el botón "View on Azure Marketplace" apunta a `#`, y "Buy now" del hero lleva a esa sección. En Autoscaler el enlace sí es real.
2. **Oferta "pay only for what you save"** (Autoscaler, 50 % del ahorro durante 12 meses): sigue en el texto aunque el commit `a8c4c55` quitó la tarjeta de compra de Consulting. Ahora no hay botón para contratarla; confirmar si sigue vigente o añadir un enlace a contacto.
3. **"All systems self-hosted · no external dependencies"** (terminal de la portada): los productos dependen de las APIs de Azure, del registro privado y de la licencia de Marketplace. "No external dependencies" es discutible.
4. **"Azure Container Services"** (Autoscaler, tarjeta *Self-hosted*): es un nombre de producto retirado. Probablemente se refiere a Azure Container Apps o Azure Container Instances.
5. **Multidimensional scaling** menciona "CPU, memory, IOPS, available storage", pero la lista de dimensiones soportadas no incluye memoria ni CPU como tal (sí CoreCount, Dtu, Iops, MaxDataBytes, ProvisionedStorage…). Revisar.
6. **Licencias de Traefork**: se afirma "Only permissive open-source licenses are included" (MIT / Apache 2.0). **Verificar la licencia de Sablier**: creo que el repositorio de Sablier se publica bajo AGPL-3.0, que no es permisiva. Si es así, esa frase y la tabla serían incorrectas.
7. **Plazos de respuesta distintos**: Consulting promete "within one business day" y Support "as soon as we can", aunque es el mismo formulario y el mismo endpoint. Unificar si el compromiso es el mismo.
8. **Storage Observer**:
   - "real-time view" choca con un modelo de escaneos periódicos.
   - "reclaim wasted capacity automatically" sugiere que borra archivos, cosa que no aparece en ninguna captura.
   - "forecast when you will hit capacity limits" no se muestra en ninguna parte.
   Confirmar las tres funciones o suavizar el texto.
9. **Monedas mezcladas**: Autoscaler en €, Traefork en $, capturas de Storage Observer en $. Si es intencionado (precios de lista de Azure por región), conviene indicarlo.
10. **Precios con fecha**: los de Azure (P4/P1 West Europe, Front Door, Log Analytics, D4s_v5) cambian. Recomendable añadir "List prices as of <mes/año>".
11. **Portada**: la tarjeta de Autoscaler muestra "Available on Microsoft Azure Marketplace", pero la de Storage Observer no, aunque también se vende por Marketplace.

### Cálculos comprobados (correctos)

- Autoscaler: €1,606 − €760 = €846/mes; × 12 = €10,152; 846 / 1,606 ≈ 53 %.
- Traefork:
  - 5 M peticiones/día × 30 = 150 M; 150 × $1.50 = $225; $330 + $225 = $555.
  - 600 GB × $0.083 = $49.80; Front Door total = $607.80.
  - Traefork: (600 − 100) × $0.08 = $40; $40 + $103.58 = $143.58.
  - Diferencia: $464.22/mes; × 12 ≈ $5,571.
