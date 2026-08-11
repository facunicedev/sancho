# Sancho

**Un arnés para Claude Code, para gente cuyo trabajo no es programar.**

Excels. Informes para un jefe que lee el primer párrafo. Correos a empresas que te deben una respuesta. Ese trabajo.

[English](README.md) · Licencia MIT · v0.1

---

## Quién es Sancho

Don Quijote ve cuarenta gigantes en el llano y arremete. Sancho Panza, que va a su lado, dice la frase sobre la que gira el libro entero:

> «Mire vuestra merced que aquellos que allí se parecen no son gigantes, sino molinos de viento.»

Tiene razón, lo dice sin adornos, y se sube al burro igual.

Ese es el oficio. No el héroe. El que guarda los papeles, señala el molino y cabalga al lado.

Tres cosas más sobre Sancho, y no son adorno, son el diseño:

**Habla en refranes.** Los encadena uno detrás de otro hasta que Don Quijote le suplica que pare. Cada uno es un trozo pequeño de conocimiento que a alguien le costó algo, con su motivo detrás. Este repositorio es un montón de ellos. Están en `rules/`.

**Gobierna una ínsula, y lo hace bien.** En la segunda parte le entregan la Ínsula Barataria como burla. La gobierna diez días, resuelve pleitos con sentido común sin brillo, y se marcha por su propio pie porque el cargo no vale lo que cuesta. El escudero resulta competente cuando le dan algo de verdad. Y sabe cuándo parar, que es más raro.

**Los dos cambian.** A lo largo de dos volúmenes Sancho se vuelve más idealista y Don Quijote más práctico. Los estudiosos le pusieron nombre: *sanchificación* y *quijotización*. Es el caso documentado más antiguo de dos partes que aprenden la una de la otra trabajando juntas, publicado en 1605, y es exactamente lo que este repositorio intenta hacer contigo.

Además está en dominio público. Ningún abogado de marcas ha mandado nunca una carta por Sancho Panza.

---

## Qué pasa de verdad cuando lo instalas

Sancho te hace una pregunta. No un formulario, no un recorrido de bienvenida, una pregunta:

> **¿En qué idioma trabajo?**

Después crea tus carpetas en ese idioma, te dice qué ha creado, y se calla hasta que le des trabajo.

Ya está. No te pregunta tu nombre, ni tu puesto, ni tu sector, ni para qué piensas usarlo. Eso lo deduce del trabajo. Un cuestionario de arranque lo contesta una sola vez, mal, alguien que todavía no ha empezado.

---

## Por qué existe

Ya tienes Claude Code. Está bien. También se le olvida todo en cuanto cierras la ventana, y para el trabajo de oficina eso sale mal de cuatro maneras concretas:

**Explicas tus preferencias otra vez cada sesión.** Justifica el texto. Fórmulas, no números pegados. No me mandes un markdown, que mi jefe usa Word. A la cuarta dejas de pedirlo.

**Se equivoca en los números con mucha seguridad.** No a menudo, pero una cifra mal en un informe la encuentra quien lo lee, que es el peor momento posible.

**Se acumulan archivos sin dueño.** `informe_v2_final_FINAL.docx`. Ya sabes qué carpeta.

**No se acumula nada.** El martes resuelves un problema bien y el viernes lo resuelves desde cero, un poco peor.

Sancho arregla esas cuatro, en ese orden. No con ingenio. Con archivar.

---

## Las palabras que usa este repositorio

Hay cinco tipos de pieza y se confunden constantemente entre sí. Esta es la clasificación entera, con la prueba para saber cuál necesitas.

| Pieza | Qué es | Nace cuando | Falla cuando |
|---|---|---|---|
| **Regla** | Un dato o una preferencia, escrita una vez, en una ficha | Quieres que algo se recuerde | Se convirtió en un procedimiento y sigue archivada como regla |
| **Hook** | Un guion pequeño que el programa ejecuta solo, en un momento fijo | Una máquina puede contestar sí o no, y equivocarse estropea un entregable | Necesita criterio. Entonces era una regla |
| **Skill** | Un procedimiento escrito, que se carga cuando toca | El mismo procedimiento se ha hecho tres veces | Su descripción se solapa con otra y ninguna sabe a quién le toca |
| **Agente** | Un trabajador con su propio contexto, al que llamas para que vaya y vuelva con una respuesta | Lanzas al mismo trabajador con las mismas instrucciones una y otra vez | Esperas que actúe solo. A un agente hay que llamarlo |
| **Comando** | Una petición larga que te cansaste de teclear | Escribes lo mismo otra vez, y la acción publica, borra o gasta dinero | Nadie lo teclea |

**Una regla es un sustantivo. Una skill es un verbo. Un hook es un despertador. Un agente es un empleado. Un comando es un atajo.**

Lo importante está en la columna del medio: **tres repeticiones**. No una. Una repetición es una casualidad, dos es un patrón que te has imaginado, tres es un procedimiento. Todo lo que hay aquí que no sea una regla tuvo que pasar tres veces antes.

---

## Por qué viene con cero skills

Esta es la decisión que la gente discute, así que va el razonamiento.

Una skill es el procedimiento de otro para el trabajo de otro. El mío dice que el informe va a una oficina comercial española y que las cifras van en euros con coma decimal. El tuyo no. Una skill que yo escribo para mi trabajo y te instalo en el tuyo no es una función, es la costumbre de un desconocido metida en tu repositorio, y vas a perder más tiempo peleándote con ella del que habrías tardado en escribirla.

Y no lo sostiene mi opinión, lo sostiene la medición. Las skills curadas por una persona suben el acierto de forma clara. Las que un modelo se escribe solo no aportan nada de media. La diferencia no está en la redacción, está en quién decidió que valía la pena escribirla.

Así que Sancho trae el **método** para hacer skills, no las skills. `WORKFLOW.md` te dice cuándo nace una, cómo comprobar que funciona y cómo detectar que dos se pisan. Después, tu tercera repetición de algo produce una skill que es tuya, sobre tu trabajo, en tu idioma.

Por lo mismo aquí no hay mercado de complementos ni lista de integraciones. Si quieres cien procedimientos para un trabajo que nadie ha descrito, eso ya existe en otro sitio.

Las reglas son otra cosa, y esas sí vienen encendidas. Una regla no es un procedimiento, es una opción por defecto, y las de aquí son las que el trabajo de oficina necesita sea cual sea la oficina.

---

## Qué viene encendido

Las reglas de serie, en `rules/`, indexadas a una línea cada una en `MEMORY.md`. Todas se ganaron equivocándose antes. Las que más pesan el primer día:

- **Toda cifra la calcula un guion**, y el guion se guarda junto a su salida. Nada de cuentas de cabeza ([R01](rules/R01_calculations_in_python.md)).
- **Los números de una hoja de cálculo son fórmulas vivas** contra una hoja de datos crudos, nunca valores pegados ([R03](rules/R03_excel_formulas.md)).
- **Los Word salen justificados**, con márgenes en pulgadas ([R02](rules/R02_justified_word.md)).
- **Se comprueba el archivo final, no el guion que lo hizo.** El número de páginas vive en el PDF ([R17](rules/R17_verify_the_output.md)).
- **Nada se cierra sin que lo digas tú, con palabras.** Un checklist completo no es un permiso ([R05](rules/R05_approval_to_close.md)).
- **Foros antes que notas de prensa.** La respuesta oficial a «¿esto importa?» siempre es que sí, porque alguien lo vende ([R06](rules/R06_search_before_acting.md)).
- **En cuanto editas un documento a mano, deja de regenerarse** y pasa a parchearse ([R14](rules/R14_patch_dont_regenerate.md)).
- **Toda decisión se explica en términos normales.** El tecnicismo va detrás, entre paréntesis ([R35](rules/R35_plain_language.md)).
- **Se te avisa de cuándo limpiar la sesión**, en cuanto lo que vale la pena guardar está escrito en un archivo ([R36](rules/R36_clear_the_session.md)).

**Para apagar una, dilo.** La ficha se va al archivo con su fecha y su motivo. No se borra nada, porque dentro de cuatro meses vas a querer saber por qué cambiaste de idea.

---

## Las cosas que funcionan solas

Todo lo demás en Sancho es una instrucción escrita, o sea que depende de que el modelo se acuerde. Estas no. **Tres avisan y dos impiden**, y esa diferencia es todo el diseño.

**`line_caps.py`** vigila el tamaño de los archivos en cada escritura. Cuando tu bitácora pasa de 250 líneas, lo dice. La respuesta nunca es subir el límite. La respuesta es que toca resumir, y te nombra el comando que lo hace.

**`repo_sweep.py`** corre al terminar cada turno y denuncia lo que está fuera de sitio: un archivo sin fila en ningún índice, un índice que apunta a algo que ya no existe, una bandeja de entrada que nadie vació, una regla copiada en dos sitios.

**`coherence.py`** también corre al terminar el turno, y caza los archivos que se contradicen: una ruta citada en un documento que no está en el disco, una frase que dice «las 32 reglas» habiendo 36 fichas, un historial creciendo dentro de un archivo que debería decir cómo se trabaja hoy.

Esos tres solo saben avisar. **Los dos de abajo paran el trabajo de verdad**, y son los que conviene entender antes de instalar esto.

**`the_gate.py` es el motivo de que tengas que teclear `/sign`.** Hasta que no lo hagas, no se escribe nada en tus carpetas de documentos, cálculos ni entregables. El asistente puede investigar, preparar y proponer; producir no. Cuando tecleas `/sign`, el checklist de `HANDOFF.md` se congela tal como está, y la firma vale solo para ese checklist y esa sesión: si la lista cambia, caduca sola.

**Si te ves bloqueado y no sabes por qué, la llave es `/sign`.**

**`research_guard.py`** impide que la conversación principal investigue por su cuenta en vez de pasárselo al agente `researcher`. La primera búsqueda suelta pasa; la segunda no, porque dos búsquedas seguidas ya son una investigación, y investigar en el hilo principal cuesta muchas veces lo que cuesta dentro de un agente.

**Ninguno de los dos bloqueos se fía de nada que escriba el modelo.** Ese es justo el punto: una puerta que lee un archivo escrito por aquel a quien vigila no es una puerta. `the_gate.py` se apoya en un mensaje tuyo, y `research_guard.py` en la identidad de quien llama, que la pone el propio programa. Cada hook trae su `--selftest`, y lo que prueban es la propiedad, no la aritmética:

```bash
python .claude/hooks/the_gate.py --selftest
```

Ningún hook mueve ni borra tus archivos. Un hook que actúa por su cuenta en el ordenador de otro es como se consiguen mensajes de desconocidos a medianoche.

---

## Los cuatro archivos que recuerdan

Cada uno contesta a una sola pregunta. Si dos contestan a la misma, se separan con el tiempo y ya no puedes fiarte de ninguno.

| Archivo | Pregunta |
|---|---|
| `HANDOFF.md` | ¿Dónde se quedó la última sesión? |
| `Documents/TASKS.md` | ¿Qué se hizo en cada tarea? |
| `MEMORY.md` | ¿Cómo hay que trabajar con esta persona? |
| `Knowledge/PROFILE.md` | ¿Quién es? |

El perfil lo escribe Sancho, sobre ti, a partir del trabajo. Léelo. Va a estar mal en algo y vas a querer corregirlo.

---

## Cómo aprende

No escribiendo cosas en su propia memoria. Ese es el fallo de todos los montajes que se automejoran: se llenan el contexto de sus propias suposiciones y empeoran de una forma que nadie nota.

En vez de eso, cuando una tarea produce algo reutilizable, aterriza en `Proposals/` como un archivo que lees y apruebas o tiras. Entonces, y solo entonces, se convierte en regla ([R27](rules/R27_harvest_proposes.md)).

Cada diez tareas, o cuando la bitácora se hace larga, corre `/synthesis`. Reescribe la bitácora de forma que el resumen **sustituya** al detalle en vez de apilarse encima, reconstruye la tabla de decisión desde cero, y manda al agente `architect` a revisar la maquinaria: si los hooks siguen vivos, qué archivos están cerca de su límite, qué regla lleva tres meses sin tocarse, qué aviso lleva semanas ignorado.

El arquitecto deja tres propuestas como mucho. Si tiene cinco, las dos peores no eran propuestas.

---

## Instalación

Necesitas [Claude Code](https://claude.com/claude-code) y Python 3 en tu ordenador. Nada más. Ni paquetes, ni claves, ni cuenta, ni servidor.

```bash
git clone https://github.com/facunicedev/sancho.git mi-trabajo
cd mi-trabajo
rm -rf .git && git init
claude
```

El `rm -rf .git && git init` es para que tu trabajo tenga su propio historial y no quede enredado con el de este repositorio. Tus archivos no vuelven aquí nunca.

Después Claude te hace la pregunta del idioma, y empiezas.

---

## Qué no es

No es una aplicación. No es un servicio. No envuelve nada. Es una carpeta con markdown dentro, y te lo lees entero en veinte minutos.

No es un CRM, ni un gestor de proyectos, ni un sistema de notas. Convive con lo que ya uses.

No es un agente autónomo. No manda tus correos. Escribe el borrador y para, porque lo único en lo que coincide todo el que ha probado lo contrario es que automatizar un proceso sin validar reproduce el fallo más rápido y más caro.

No está terminado. Esto es la v0.1, sacada de un repositorio real con diecisiete tareas reales detrás. Lo que hay aquí se ha usado. Lo que no se ha usado no está.

---

## Contribuir

Lee [CONTRIBUTING.md](CONTRIBUTING.md). En corto: la contribución que interesa es una regla que te costó algo aprender, con la historia de lo que salió mal pegada detrás. Una regla sin cicatriz es una suposición.

## Licencia

MIT. Está en [LICENSE](LICENSE). Haz con esto lo que quieras.
