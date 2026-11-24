"""Contenido del portafolio. Para sumar un proyecto, agregar un dict a PROYECTOS y correr build.py.

Regla: todo anonimo. Sin nombres de clientes ni de la empresa, y capturas con datos inventados.
"""

PERFIL = {
    "marca": "DGLab",
    "nombre": "Agustín Denicola",
    "rol": "Software y soluciones digitales personalizadas",
    "titulo": "Software a medida para negocios que quieren trabajar mejor.",
    "bajada": (
        "Convertimos ideas, procesos y problemas en soluciones digitales simples, útiles, productivas y hechas a medida: "
        "sistemas de gestión, turnos, pedidos online, mapeos y automatizaciones con IA, entre otras."
    ),
    "fundador": (
        "DGLab es la consultora liderada por Agustín Denicola. Trabajamos de manera personalizada con cada cliente "
        "desde la primera conversación hasta tener la solución en producción."
    ),
    "zona": "Estés donde estés, podemos trabajar juntos. Presencial o virtualmente.",
    "sobre_mi": (
        "Desarrollo sistemas a medida para negocios. Me ocupo de todo el "
        "proceso: entender cómo trabajás, diseñar, programar, publicar y acompañarte después. "
        "No hay intermediarios: hablás siempre conmigo."
    ),
    "email": "labdglab@gmail.com",
    "whatsapp": "5493487207561",  # formato wa.me: 549 + caracteristica + numero
    "linkedin": "",  # ej: "https://www.linkedin.com/in/usuario"
    "github": "",  # los repos de clientes son privados; sumar solo si hay proyectos publicos
}

PROYECTOS = [
    {
        "slug": "gestion-agencia-autos",
        "titulo": "Sistema de gestión para agencia de autos",
        "resumen": "Centralización de compras, gastos, socios inversores y liquidaciones automáticas, con un portal para que cada inversor vea solo lo suyo.",
        "rubro": "Automotriz",
        "portada": "agencia-panel.webp",
        "problema": (
            "La agencia llevaba todo en un Excel: qué auto compró cada socio, quién pagó cada gasto y cuánto le "
            "correspondía a cada uno al vender. Calcular una liquidación llevaba tiempo y era fácil equivocarse."
        ),
        "solucion": [
            "Ficha por auto con compra, gastos, venta y resultado.",
            "Liquidación automática por socio: aporte + gastos que pagó + parte del resultado, con estado pendiente, calculada o pagada.",
            "Consignaciones: los gastos se recuperan de la venta y la agencia cobra su comisión.",
            "Portal para inversores externos: cada uno entra con su usuario y ve solo sus autos.",
            "Historial de cambios con valor anterior y nuevo, comprobantes adjuntos (foto o PDF) y reportes mensuales con descarga.",
            "Usuarios por rol, recuperación de acceso por WhatsApp y copias de seguridad automáticas semanales.",
        ],
        "resultado": "Publicado con dominio propio. Al migrar, la app detectó gastos sin monto y un cálculo de consignaciones que en el Excel daba mal.",
        "imagenes": [
            ("agencia-panel.webp", "Panel operativo con autos que necesitan atención y estado de la cartera"),
            ("agencia-liquidacion.webp", "Ficha de un auto vendido con la liquidación de cada socio"),
            ("agencia-reportes.webp", "Reporte del período: ventas, resultado, gastos por categoría y pagos"),
            ("agencia-mobile-inversor.webp", "Portal del inversor desde el celular"),
            ("agencia-historial.webp", "Historial de cambios con el detalle de qué cambió"),
        ],
    },
    {
        "slug": "consumos-hoteles",
        "titulo": "Control de consumos para cadena de hoteles",
        "resumen": "Agua, luz y gas de varios hoteles en un solo lugar: consumo por huésped, alertas y comparación entre hoteles.",
        "rubro": "Hospitalidad y turismo",
        "portada": "hoteles-inicio.webp",
        "problema": (
            "Las facturas de agua, luz y gas de cada hotel llegaban en PDF y se pasaban a mano a planillas. "
            "No había forma rápida de saber si un hotel estaba consumiendo de más ni de comparar entre hoteles."
        ),
        "solucion": [
            "Lectura automática de las facturas en PDF: se arrastran y el sistema toma consumo, período e importe.",
            "Consumo por huésped de cada servicio, comparado con una referencia y con el año anterior.",
            "Comparación entre hoteles mes a mes, con gráficos y tablas.",
            "Informes en PDF y Excel listos para presentar a los dueños, armados con las secciones que se elijan.",
            "Alertas propias para vencimientos y pendientes, papelera y copias de seguridad automáticas.",
        ],
        "resultado": (
            "Una herramienta instalada en la computadora de la gestora que reemplaza las planillas, detecta consumos fuera "
            "de lo normal y arma los informes para los dueños en minutos."
        ),
        "imagenes": [
            ("hoteles-inicio.webp", "Inicio: consumo por huésped de cada hotel y alertas"),
            ("hoteles-servicio.webp", "Detalle de un servicio con consumo mensual y por huésped"),
            ("hoteles-comparar.webp", "Comparación entre hoteles frente a la referencia"),
        ],
    },
    {
        "slug": "turnos-online-barberia",
        "titulo": "Sistema de turnos para servicios de cuidado personal y estética",
        "resumen": "Los clientes reservan, modifican o cancelan sus turnos. El profesional gestiona y organiza su agenda desde el celular.",
        "rubro": "Cuidado personal y estética",
        "portada": "barberia-reserva.webp",
        "foco": "right top",
        "problema": (
            "La coordinación manual de turnos dificultaba la organización diaria, generaba reservas superpuestas y "
            "aumentaba las ausencias por olvidos o falta de recordatorios."
        ),
        "solucion": [
            "Reserva en tres pasos: servicio, horario libre y datos de contacto.",
            "Cada reserva ocupa el bloque según la duración del servicio, sin superposiciones.",
            "Link por mail para modificar o cancelar, y recordatorio automático 3 horas antes.",
            "Panel de administración: días y horarios, descansos, servicios, precios y agenda en vivo.",
        ],
        "resultado": (
            "La aplicación se publicó bajo un dominio propio y se configuró el envío automático de correos electrónicos "
            "desde la dirección institucional del negocio, reforzando su identidad y profesionalismo."
        ),
        "imagenes": [
            ("barberia-reserva.webp", "Pantalla de reserva con horarios disponibles"),
            ("barberia-mobile.webp", "Reserva desde el celular"),
        ],
    },
    {
        "slug": "landing-tienda-online",
        "titulo": "Landing 3D para tienda online",
        "resumen": "Una presentación de producto con modelos 3D que giran al deslizar, conectada a la tienda online para comprar.",
        "rubro": "Comercio",
        "portada": "tienda-portada.webp",
        "problema": (
            "Un emprendimiento de botellas reutilizables vendía por su tienda online, pero las fotos de catálogo no "
            "transmitían la calidad del producto ni lo diferenciaban de la competencia."
        ),
        "solucion": [
            "Modelos 3D de cada producto que giran y se acercan a medida que se recorre la página.",
            "Diseño premium con tipografía editorial y animaciones suaves.",
            "Botones de compra que llevan directo a cada producto en la tienda online.",
            "Pensada para verse y andar fluida también en el celular.",
        ],
        "resultado": "Una vidriera Web que presenta los productos con identidad propia y deriva la venta a la tienda online.",
        "imagenes": [
            ("tienda-portada.webp", "Portada con los dos productos en 3D"),
            ("tienda-producto.webp", "Sección de marca con los productos girando"),
        ],
    },
    {
        "slug": "pedidos-online-farmacia",
        "titulo": "Web y pedidos online para farmacia",
        "resumen": "Promociones, turnos y un formulario que arma el pedido completo para enviarlo por WhatsApp.",
        "rubro": "Salud",
        "portada": "farmacia-inicio.webp",
        "problema": (
            "Los pedidos llegaban por WhatsApp con información incompleta: modalidad de entrega, forma de pago, obra social "
            "y requisitos de receta. Esto generaba intercambios adicionales y complicaba la organización."
        ),
        "solucion": [
            "Web con promociones, categorías, horarios y turnos.",
            "Formulario de pedido que arma un mensaje ordenado de WhatsApp con entrega, pago, obra social y receta.",
            "Panel interno para cargar productos, publicar promociones y actualizar turnos.",
            "Diseño pensado primero para el celular.",
        ],
        "resultado": "Una Web pública para recibir pedidos y un panel interno para centralizar la información y facilitar su gestión.",
        "imagenes": [
            ("farmacia-inicio.webp", "Portada de la web"),
            ("farmacia-pedido.webp", "Formulario de pedido online"),
            ("farmacia-admin.webp", "Panel interno para productos y promociones"),
            ("farmacia-mobile.webp", "Vista desde el celular"),
        ],
    },
    {
        "slug": "mostrador-corralon",
        "titulo": "Mostrador, stock y presupuestos para comercio",
        "resumen": "Más de 1.300 productos con búsqueda por código o por cómo los pide el cliente, presupuestos, ventas y cierres de caja.",
        "rubro": "Comercio",
        "portada": "corralon-mostrador.webp",
        "problema": "Precios en listas de proveedores, stock de memoria y presupuestos a mano. En el mostrador se perdía tiempo buscando cada producto.",
        "solucion": [
            "Búsqueda por código propio, nombre, medida o la forma en que lo pide el cliente.",
            "Presupuestos y ventas con cálculo de totales, descuentos y datos fiscales cuando corresponde.",
            "Control y descuento de stock, ubicación de cada producto y tickets de cierre.",
            "Actualización de precios importando las listas de los proveedores.",
        ],
        "resultado": "Herramienta local para el mostrador: corre en la compu del negocio, sin depender de Internet.",
        "imagenes": [("corralon-mostrador.webp", "Mostrador: búsqueda de productos y armado de presupuesto")],
    },
    {
        "slug": "avisos-cortes-municipio",
        "titulo": "Avisos de cortes por WhatsApp para un municipio",
        "resumen": "Recibe los avisos de cortes desde grupos de WhatsApp, los interpreta con IA y los muestra en panel, dashboard e historial.",
        "rubro": "Gobierno",
        "portada": "municipio-dashboard.webp",
        "problema": (
            "Los avisos de cortes de servicios se recibían por WhatsApp en distintos formatos, como mensajes de texto e imágenes. "
            "La información quedaba dispersa, sin un registro centralizado ni una visión general que facilitara su consulta y seguimiento."
        ),
        "solucion": [
            "Conector con grupos de WhatsApp autorizados.",
            "Interpretación de texto e imagen para clasificar el aviso: imprevisto, programado o restablecido.",
            "Detección de zona por texto o por calles, y cruce con instituciones sensibles (escuelas, centros de salud).",
            "Panel operativo, dashboard con tiempos de resolución, mapa, historial y exportación a Excel.",
        ],
        "resultado": "Solución que centraliza y organiza los avisos, facilita su consulta y permite visualizar la información de manera integrada.",
        "imagenes": [("municipio-dashboard.webp", "Dashboard de cortes con estados, tipos y tiempos de resolución")],
    },
    {
        "slug": "relevamiento-industrial",
        "titulo": "App de relevamiento industrial en campo",
        "resumen": "Guía al técnico equipo por equipo, con fotos obligatorias y datos, sin necesidad de Internet.",
        "rubro": "Industria",
        "portada": "relevamiento-crear.webp",
        "problema": (
            "Los relevamientos en planta se realizaban mediante planillas y fotografías almacenadas por separado en los celulares. "
            "La información quedaba dispersa y requería mucho tiempo de trabajo posterior para organizarla, consolidarla y consultarla."
        ),
        "solucion": [
            "Carga de la lista de equipos desde un archivo, con detección automática de columnas.",
            "Recorrido tag por tag con campos configurables y fotos obligatorias (lejos, cerca, tag y placa).",
            "Funciona offline en tablet o celular y muestra el progreso del relevamiento.",
            "Exportación ordenada: carpeta y ZIP con resumen y fotos por equipo.",
        ],
        "resultado": (
            "Solución disponible como aplicación Web instalable (PWA) y aplicación Android con funcionamiento offline, "
            "que permite realizar relevamientos directamente en planta, incluso sin conexión a Internet."
        ),
        "imagenes": [("relevamiento-crear.webp", "Creación de un relevamiento a partir de la lista de equipos")],
    },
    {
        "slug": "generador-mel-ocr",
        "titulo": "Lista maestra de equipos a partir de fotos",
        "resumen": "Lee los tags de los equipos en las fotos del relevamiento y arma la planilla oficial automáticamente.",
        "rubro": "Industria",
        "portada": "",
        "icono": "OCR",
        "problema": (
            "Después de cada relevamiento había que mirar foto por foto, anotar el tag de cada equipo y copiar a mano "
            "sus datos en la lista maestra (MEL), con el riesgo de errores de tipeo y filas mal copiadas."
        ),
        "solucion": [
            "Se suben las fotos del relevamiento y el sistema lee el tag de cada equipo.",
            "Cada tag se busca en la base de equipos y se copia la fila completa, con la misma estructura oficial.",
            "Los casos dudosos pasan a una tabla de revisión para validarlos o corregirlos.",
            "Descarga de la nueva MEL en Excel, con una hoja de trazabilidad de cada foto.",
        ],
        "resultado": "Solución que convierte las fotos del relevamiento en la lista maestra de equipos, con control humano solo donde hace falta.",
        "imagenes": [],
    },
    {
        "slug": "dashboard-monitoreo-operativo",
        "titulo": "Dashboard de monitoreo operativo",
        "resumen": "Una sola pantalla para ver eventos, riesgos, cumplimiento de SLA y alertas de una operación industrial.",
        "rubro": "Industria",
        "portada": "dashboard-monitoreo.webp",
        "problema": (
            "La información de la operación llegaba por distintos canales —WhatsApp, sensores, formularios y correos electrónicos— "
            "y estaba dispersa. Se necesitaba centralizarla en una única vista para facilitar su consulta, seguimiento y análisis."
        ),
        "solucion": [
            "Indicadores clave: eventos detectados, riesgo alto, SLA, tiempo medio de respuesta e informes automatizados.",
            "Tendencia diaria de eventos por severidad y ranking de riesgo por área.",
            "Alertas recientes y mapa de criticidad por frecuencia e impacto.",
            "Estado de los canales integrados: WhatsApp, sensores, formularios y correos electrónicos.",
        ],
        "resultado": "Diseño y desarrollo de una solución de visualización centralizada con información ordenada y lista para la toma de decisiones.",
        "imagenes": [("dashboard-monitoreo.webp", "Vista general del dashboard de monitoreo")],
    },
    {
        "slug": "asistente-ia-documentacion",
        "titulo": "Asistente de IA sobre documentación técnica",
        "resumen": "Responde preguntas usando exclusivamente los manuales técnicos específicos de la organización.",
        "rubro": "Industria",
        "portada": "",
        "icono": "IA",
        "problema": (
            "Consultar manuales técnicos de cientos de páginas para encontrar un dato específico demandaba mucho tiempo "
            "y dificultaba el acceso ágil a la información."
        ),
        "solucion": [
            "Carga de los manuales en PDF y búsqueda por significado, no solo por palabras exactas.",
            "Respuestas basadas exclusivamente en la documentación cargada.",
            "Preguntas de prueba para medir y mejorar la calidad de las respuestas.",
            "Una Web simple donde el equipo pregunta como le preguntaría a un colega.",
        ],
        "resultado": (
            "Solución de consulta inteligente: un asistente Web donde el equipo hace su pregunta en lenguaje natural "
            "y recibe la respuesta basada en sus propios manuales."
        ),
        "imagenes": [],
    },
    {
        "slug": "marca-de-agua-automatica",
        "titulo": "Marca de agua automática para documentos",
        "resumen": "Los documentos que se suben a una carpeta compartida salen con la marca de agua de la empresa, sin pasos manuales.",
        "rubro": "Empresas",
        "portada": "",
        "icono": "MA",
        "problema": (
            "Cada documento que se entregaba a un cliente requería incorporar manualmente la marca de agua propia de la empresa. "
            "El proceso debía repetirse archivo por archivo, consumiendo tiempo y esfuerzo operativo."
        ),
        "solucion": [
            "Procesamiento automático de imágenes y documentos.",
            "Integración con las carpetas compartidas de la empresa.",
            "Versión Web para usarla desde el navegador y funcionamiento automático en segundo plano.",
        ],
        "resultado": "Solución automatizada para incorporar marcas de agua en los documentos.",
        "imagenes": [],
    },
    {
        "slug": "cuentas-claras",
        "titulo": "App de finanzas para el hogar",
        "resumen": "Ingresos, egresos, gastos fijos y tarjetas en cuotas, con recordatorios en el celular y logros para sostener el hábito.",
        "rubro": "Finanzas personales",
        "portada": "cuentas-inicio.webp",
        "problema": (
            "Llevar las cuentas de la casa en un cuaderno o en una planilla se abandona rápido: cuesta anotar cada gasto, "
            "las cuotas de las tarjetas se pierden de vista y a fin de mes no queda claro en qué se fue el dinero."
        ),
        "solucion": [
            "«Anotá rápido»: se escribe «súper 45 mil» y el gasto queda cargado.",
            "Saldo disponible del mes y cuánto se puede gastar por día.",
            "Tarjetas de crédito con cuotas, cierres, vencimientos y lo comprometido en los próximos meses.",
            "Recordatorios en el celular, racha de días y logros para que anotar se vuelva costumbre.",
            "Se instala en el celular como una app, con cuentas privadas y suscripción con Mercado Pago.",
        ],
        "resultado": "Una aplicación Web instalable, cálida y fácil de usar, pensada para personas que nunca usaron una app de finanzas.",
        "imagenes": [
            ("cuentas-inicio.webp", "Inicio con el saldo del mes y la carga rápida"),
            ("cuentas-mobile.webp", "Vista desde el celular"),
            ("cuentas-tarjetas.webp", "Tarjetas y cuotas comprometidas"),
            ("cuentas-logros.webp", "Logros y racha de días"),
        ],
    },
    {
        "slug": "app-finanzas-y-rutina",
        "titulo": "Productividad y gestión personal",
        "resumen": "Dinero, trabajo, estudio y hábitos saludables en un solo lugar, con cierres mensuales exportables a Excel.",
        "rubro": "Uso personal",
        "portada": "finanzas-plata.webp",
        "problema": (
            "Finanzas, horas de trabajo, objetivos de ahorro y actividades de estudio se gestionaban por separado, "
            "dificultando la organización y el seguimiento de los objetivos personales."
        ),
        "solucion": [
            "Ingresos y gastos por categoría, con cierre mensual exportable a Excel.",
            "Ahorros e inversiones con objetivos y avance.",
            "Registro de jornada con horas normales y extra, bloques de estudio y seguimiento del gimnasio.",
            "Recordatorios periódicos para no cortar la rutina.",
        ],
        "resultado": (
            "Una aplicación que integra toda la gestión personal en un solo lugar, funciona sin conexión a Internet "
            "y guarda la información localmente en el navegador."
        ),
        "imagenes": [
            ("finanzas-plata.webp", "Ingresos y gastos del mes"),
            ("finanzas-ahorros.webp", "Ahorros e inversiones con objetivos"),
            ("finanzas-mobile.webp", "Inicio desde el celular"),
        ],
    },
]

SERVICIOS = [
    ("Sistemas a medida", "Herramientas de gestión adaptadas a la forma real de trabajar de tu equipo."),
    ("Automatización", "Menos tareas repetitivas, menos errores y más tiempo para lo importante."),
    ("Datos e inteligencia artificial", "Tableros, reportes e IA para comprender mejor el negocio, optimizar procesos y decidir con información."),
    ("Mapas y relevamientos", "Mapas interactivos, recorridos y visualización de información de campo."),
]

PROCESO = [
    ("Entendemos cómo trabajás", "Miramos tu Excel, tus mensajes y tu día a día antes de proponer nada."),
    ("Prototipo rápido", "Ves una primera versión funcionando con tus propios datos."),
    ("Ajustes con uso real", "La usás, nos contás qué falta y lo corregimos."),
    ("Online y con soporte", "Queda publicada, con copias de seguridad y soporte."),
]

# "Arma tu consulta": opciones que el cliente toca para armar el mensaje de WhatsApp.
RUBROS = [
    "Automotriz", "Comercio", "Gobierno", "Hospitalidad y turismo", "Industria",
    "Salud, cuidado personal y estética", "Otro",
]
NECESIDADES = [
    "Ordenar stock y ventas",
    "Turnos online",
    "Pedidos por WhatsApp",
    "Reemplazar un Excel",
    "Ver mis números claros",
    "Automatizar tareas",
    "Usar inteligencia artificial",
    "Una página Web",
]

PREGUNTAS = [
    ("¿Tengo que saber de computación?", "No. Diseñamos pensando en quien la va a usar todos los días, en la compu o en el celular."),
    ("Ya uso un Excel u otro sistema, ¿empiezo de cero?", "No. Partimos de lo que ya tenés e importamos tus datos para no perder nada."),
    ("¿Los datos son míos?", "Sí. La información es tuya, con copias de seguridad, y la podés descargar en Excel cuando quieras."),
    ("¿Hace falta reunirnos en persona?", "No. Podemos hacer todo por videollamada y WhatsApp, y si preferís, también en persona."),
]
