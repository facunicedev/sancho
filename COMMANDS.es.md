# Comandos

> **Para qué sirve este archivo.** Lo que puedes teclear, y lo que pasa sin que teclees nada, en una hoja. Los comandos viven en `.claude/commands/`; aquí solo se dice qué hace cada uno, no cómo.
>
> [In English](COMMANDS.md)

## Lo que tecleas

| Comando | Qué hace | Cuándo |
|---|---|---|
| `/sign` | Firma el checklist de la tarea en curso y abre la puerta de producción | Cuando has leído el checklist y estás de acuerdo |
| `/approve` | Aplica las propuestas que nombres de `Proposals/`, las borra y lanza al `architect` detrás | Cuando una propuesta te parece bien |
| `/notapprove` | Descarta las propuestas que nombres, con el motivo escrito en la bitácora | Cuando una propuesta no te convence |
| `/left` | Dónde estamos: tarea en curso, tareas abiertas, decisiones esperando y lo que te toca a ti | Cuando quieras saberlo |
| `/synthesis` | Resume la bitácora de tareas, reformula la tabla de decisión y lanza al agente `architect` a revisar el sistema | Cada 10 tareas, o cuando el hook de topes avisa de que la bitácora se pasó de su límite |

Y uno que no es nuestro pero se usa igual: **`/clear`**, que vacía la conversación. Se ofrece solo cuando el estado ya está escrito en disco (R13), nunca antes.

**`/sign` es la llave de todo.** Hasta que no lo teclees, no se escribe nada en tus carpetas de documentos, cálculos ni entregables: el asistente puede preparar, investigar y proponer, pero no producir. Es a propósito, y es el único comando que no puedes saltarte. Es un comando y no una frase porque adivinar si un mensaje aprobaba falló dos veces con la aprobación delante.

## Lo que pasa sin teclear nada

Hooks. No hay que acordarse de ninguno: corren solos.

| Hook | Qué hace | Cuándo salta |
|---|---|---|
| `line_caps.py` | Avisa cuando un archivo de control pasa de su tope de líneas | En cada escritura |
| `repo_sweep.py` | Avisa de archivos que faltan en su índice, bandejas sin vaciar y basura olvidada | Al terminar el turno |
| `coherence.py` | Avisa de rutas citadas que no existen y de cuentas que no cuadran | Al terminar el turno |
| `the_gate.py` | **Impide** producir sin un checklist que hayas firmado, y dice cuál es el paso siguiente | Antes de escribir, al firmar y al terminar el turno |

**Tres avisan y uno impide, que es la diferencia que importa.** Un aviso se puede ignorar; un bloqueo no. Impedir se reserva a lo único que estropea el trabajo: producir antes de haber acordado qué se produce.

**Ninguno vigila lo que está en el `.gitignore`.** Quién es del repositorio lo decide git, y no una lista de nombres de carpeta escrita dentro de cada hook. Apunta un hook a un conjunto de datos descargado o a una copia de seguridad y te informará de frases que no ha escrito nadie de aquí.

## Si un comando no aparece

Teclea `/` para ver el listado. Si falta uno nuevo, reinicia la sesión: `.claude/commands/` se lee al arrancar.

## Añadir los tuyos

Un comando se gana su sitio cuando te descubres tecleando a mano la misma petición larga, y además la acción publica, borra o gasta dinero. Lo que sea más corto que eso es simplemente pedirlo. El criterio completo está en `WORKFLOW.md`, en «Cuándo nace cada pieza».
