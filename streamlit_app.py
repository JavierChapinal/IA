import streamlit as st
import pandas as pd
import numpy as np
import time
import webbrowser


def textos(texto):
    if texto == "Clasificación de Riesgos":
        return "La ley clasifica los sistemas de IA en cuatro categorías de riesgo, con regulaciones específicas para cada una:\n 1.	Riesgo Inaceptable: Estos sistemas están prohibidos debido a su potencial para causar daño significativo. Ejemplos incluyen: \n - Sistemas de Puntuación Social: Modelos que evalúan a personas basado en su comportamiento social. Estos sistemas utilizan algoritmos para evaluar la confiabilidad o el comportamiento de las personas, asignándoles una puntuación que puede afectar su acceso a servicios esenciales como préstamos, seguros o empleo. La AI Act prohíbe estos sistemas por su potencial para discriminar, manipular y controlar a las personas, especialmente a grupos vulnerables.\n - Manipulación Subliminal: Herramientas que influyen en las decisiones de los usuarios sin su conocimiento. Estos sistemas utilizan algoritmos para tomar decisiones legales o administrativas importantes, como la evaluación de la admisibilidad de pruebas, la determinación de la fianza o la predicción del riesgo de reincidencia.\n - Vigilancia masiva o la extracción de datos biométricos: Estos sistemas recopilan y analizan datos biométricos de las personas, como huellas dactilares, reconocimiento facial o ADN, para fines de vigilancia o control social. La AI Act prohíbe su uso generalizado y exige medidas de seguridad y protección de datos estrictas para este tipo de sistemas.\nExplotación de Vulnerabilidades: Tecnologías que se aprovechan de grupos vulnerables, como niños y personas con discapacidades. La AI Act prohíbe este tipo de sistemas, como juguetes que fomentan comportamientos peligrosos o chatbots que difunden información falsa o dañina. La AI Act prohíbe su uso generalizado en la administración de justicia debido a los riesgos para la imparcialidad, la transparencia y el derecho a un juicio justo.\n 2.	Riesgo Alto: Estos sistemas requieren rigurosas evaluaciones de conformidad antes de ser desplegados. Incluyen:\n - IA en Infraestructuras Críticas: Por ejemplo, redes eléctricas y sistemas de transporte para la conducción autónoma o la gestión del tráfico, donde los fallos podrían tener graves consecuencias para la seguridad pública, como por ejemplo un sistema de piloto automático utilizado por un fabricante de camiones para vehículos de transporte de larga distancia.\n - Educación y Formación: Herramientas utilizadas para evaluar el desempeño de los estudiantes.\n - Empleo y Gestión de Recursos Humanos: Sistemas que ayudan en la contratación y evaluación de empleados.\n - Servicios Esenciales: Como IA utilizada en la asistencia sanitaria, policía y justicia como sistemas para el diagnóstico o tratamiento de enfermedades de alto riesgo o la evaluación de la fianza o la predicción del riesgo de reincidencia para presidiarios.\n 3.	Riesgo Limitado: Los sistemas bajo esta categoría deben cumplir con obligaciones de transparencia, como informar a los usuarios que están interactuando con una IA.\n - Chatbots y Asistentes Virtuales: Los proveedores deben revelar que el usuario está interactuando con una máquina. Como por ejemplo un chatbot que responde preguntas frecuentes sobre productos o servicios en un sitio web de comercio electrónico.\n - Sistemas de recomendación de productos: como un sistema de IA que recomienda películas o música a los usuarios de una plataforma de streaming.\nHerramientas de análisis de datos para la optimización del marketing: sistema de IA que analiza datos de ventas para identificar patrones y tendencias que ayuden a mejorar las campañas de marketing.\n - Software de traducción automática: un servicio de traducción en línea que permite a los usuarios traducir texto de un idioma a otro.\n4.	Riesgo Mínimo: Estos sistemas están sujetos a pocas restricciones debido a su bajo potencial de causar daño. Incluyen aplicaciones de IA comunes como filtros de spam y videojuegos.\n - Calculadoras: una aplicación de calculadora básica en un teléfono inteligente.\n - Filtros de Spam: filtros que bloquean correos electrónicos no deseados basados en palabras clave o direcciones de correo electrónico conocidas.\n - Juegos de IA: como por ejemplo un juego de ajedrez que utiliza un oponente de IA.\n - Asistentes de voz básicos: un asistente de voz que puede reproducir música o configurar alarmas, pero no tiene capacidades avanzadas de comprensión del lenguaje natural.\n - Software de edición de fotos básico: aplicaciones que aplican filtros o efectos preestablecidos en las foto"
    
    elif texto == "Nuevas Instituciones y Órganos":
        return "Para asegurar la implementación y cumplimiento efectivo de la ley, se establecieron varias nuevas instituciones:\n\n**Oficina de IA**\n\nDependiente de la Comisión Europea, esta autoridad coordinará la implementación de la ley en todos los Estados Miembros y supervisará el cumplimiento por parte de los proveedores de IA de propósito general. Su trabajo contribuye a garantizar que la IA se desarrolle y utilice de manera responsable, protegiendo los derechos y la seguridad de las personas en toda Europa. Funciones principales: \n\n_Supervisión y coordinación_\n\n - La Oficina Europea de Inteligencia Artificial supervisa la aplicación de la AI Act en todos los Estados miembros de la UE.\n - Coordina las actividades de las autoridades nacionales competentes en materia de IA.\n- Facilita el intercambio de información y mejores prácticas entre las autoridades nacionales.\n\n_Orientación y asistencia_\n\n- La Oficina Europea de Inteligencia Artificial proporciona orientación y asistencia a las empresas, organizaciones y ciudadanos sobre sus obligaciones bajo la AI Act.\n- Publica directrices y documentos explicativos para facilitar la comprensión de la ley.\n- Ofrece servicios de asesoramiento y apoyo a las autoridades nacionales.\n\n_Vigilancia del mercado y cumplimiento_\n\n- La Oficina Europea de Inteligencia Artificial vigila el mercado para detectar posibles incumplimientos de la AI Act.\n- Investiga las denuncias de incumplimiento y toma las medidas oportunas, como iniciar procedimientos de sanción.\n- Colabora con las autoridades nacionales para garantizar una aplicación efectiva de la ley en toda la UE.\n\n_Cooperación internacional_\n\n- La Oficina Europea de Inteligencia Artificial colabora con organismos internacionales y socios de terceros países en materia de IA.\n- Promueve el desarrollo y la aplicación de estándares globales de IA responsables.\n- Participa en el intercambio de información y mejores prácticas con otros países.\n\n_Fomento de la innovación y la investigación_\n\n- La Oficina Europea de Inteligencia Artificial apoya la investigación y el desarrollo de IA responsable.\n- Identifica y promueve las mejores prácticas en el desarrollo y uso de la IA.\n- Facilita la interacción entre el sector público y privado para impulsar la innovación en el ámbito de la IA.\n\n**Foro Asesor**\n\nProporcionará asesoramiento técnico y representará una selección equilibrada de partes interesadas, incluyendo la industria, startups, pymes, sociedad civil y academia. El Foro Asesor está compuesto por 30 miembros seleccionados por la Comisión Europea a partir de propuestas presentadas por los Estados miembros, las organizaciones europeas de normalización y las partes interesadas relevantes. Los miembros del Foro Asesor son expertos en diversos campos relacionados con la IA, como la ética, el derecho, la tecnología, la economía y la sociedad:\n\n_Asesorar a la Comisión Europea:_ El Foro Asesor proporciona asesoramiento independiente a la Comisión Europea sobre diversos aspectos relacionados con la IA, incluyendo:\n\n- La aplicación e interpretación de la AI Act.\n- La identificación de nuevos riesgos y desafíos emergentes en el ámbito de la IA.\n- El desarrollo de políticas y medidas para promover la IA responsable y ética.\n\n_Fomentar el diálogo entre las partes interesadas:_ El Foro Asesor facilita el diálogo entre diversos actores relevantes en el ámbito de la IA, como:- Autoridades nacionales y europeas.\n- Empresas y organizaciones del sector privado.\n- La academia y la sociedad civil.\n- Representantes de los ciudadanos y grupos de interés.\n\n_Promover el intercambio de información y mejores prácticas:_ El Foro Asesor facilita el intercambio de información y mejores prácticas entre las partes interesadas, contribuyendo a:- Aumentar la comprensión de los desafíos y oportunidades de la IA.\n\n- Identificar soluciones innovadoras para desarrollar y utilizar la IA de manera responsable.\n- Fomentar la colaboración y la cooperación entre los diferentes actores.\n\n**Panel Científico de Expertos Independientes**\n\nProveerá asesoramiento técnico y alertas de riesgos potenciales a la Oficina de IA y a las autoridades nacionales. Está compuesto por un número de expertos seleccionado por la Comisión Europea sobre la base de sus conocimientos científicos y técnicos actualizados en el ámbito de la IA. Los expertos del Panel deben ser independientes de cualquier proveedor de sistemas de IA o modelos de IA de uso general y deben actuar con imparcialidad y objetividad.\n\n_Asesorar a la Comisión Europea y a la Oficina Europea de Inteligencia Artificial:_ El Panel Científico de Expertos Independientes proporciona asesoramiento científico y técnico independiente a la Comisión Europea y a la Oficina Europea de Inteligencia Artificial sobre diversos aspectos relacionados con la IA, incluyendo:\n\n- La evaluación de los riesgos y las oportunidades de los nuevos sistemas y aplicaciones de IA.\n- El desarrollo de herramientas y métodos para evaluar y verificar el cumplimiento de la AI Act.\n- La identificación de posibles sesgos y discriminaciones en los sistemas de IA.\n- La formulación de recomendaciones sobre políticas y medidas para promover la IA responsable y ética.\n\n_Emitir dictámenes científicos:_\n\n El Panel Científico de Expertos Independientes puede emitir dictámenes científicos a solicitud de la Comisión Europea, la Oficina Europea de Inteligencia Artificial o a iniciativa propia. Estos dictámenes se basan en el conocimiento científico y técnico más actualizado disponible y deben ser objetivos, imparciales y transparentes. \n\n_Colaborar con otros organismos_\n\nEl Panel Científico de Expertos Independientes puede colaborar con otros organismos de la Unión Europea y con expertos de terceros países en el ámbito de la IA."
    
    elif texto == "Evaluación de la conformidad":
        return "La Ley de Inteligencia Artificial de la Unión Europea (AI Act) establece un marco regulatorio integral para la evaluación y el uso de sistemas de IA. Los sistemas de IA de alto riesgo, aquellos que presentan un mayor potencial de daño a las personas o sus derechos, deben someterse a evaluaciones de conformidad para verificar que cumplen con los requisitos establecidos en la ley.\n\nLos requisitos de evaluación de conformidad para sistemas de IA de alto riesgo se detallan en el Anexo III del Reglamento de la Inteligencia Artificial. Estos requisitos se basan en los principios de enfoque basado en el riesgo y proporcionalidad, lo que significa que la rigurosidad de la evaluación se adapta al nivel de riesgo específico que presenta cada sistema de IA.\n\nEn general, los requisitos de evaluación de conformidad para sistemas de IA de alto riesgo incluyen:\n\n**1. Evaluación de la conformidad:**\n\n- Realizada por un organismo de evaluación independiente y acreditado\n- Implica la evaluación de la documentación técnica, el código fuente y el funcionamiento del sistema de IA\n- Debe verificar que el sistema de IA cumple con todos los requisitos establecidos en la AI Act.\n\n**2. Requisitos técnicos y organizativos**\n- El sistema de IA debe cumplir con requisitos técnicos específicos para garantizar su seguridad, fiabilidad, robustez y transparencia\n- El proveedor del sistema de IA debe implementar medidas organizativas adecuadas para gestionar los riesgos asociados al sistema de IA.\n\n**3. Documentación técnica**\n\n- El proveedor del sistema de IA debe elaborar una documentación técnica completa que describa el sistema de IA, su funcionamiento, sus riesgos y las medidas de mitigación implementadas\n- La documentación técnica debe estar disponible para las autoridades competentes y para los organismos de evaluación.\n\n**4. Procedimientos de transparencia**\n- El proveedor del sistema de IA debe proporcionar información clara y transparente a los usuarios sobre el sistema de IA, incluyendo su funcionamiento, sus capacidades y limitaciones\n- Los usuarios deben tener la posibilidad de deshabilitar o desinstalar el sistema de IA si lo desean.\n\n**5. Monitoreo y seguimiento**\n\n- El proveedor del sistema de IA debe monitorizar y seguir el rendimiento del sistema de IA para identificar y abordar cualquier problema que pueda surgir\n- El proveedor del sistema de IA debe mantener un registro de las actividades de monitoreo y seguimiento.Estas evaluaciones pueden ser realizadas por:Autoevaluación: Realizada por los proveedores de sistemas de IAEvaluación de Terceros: Realizada por organismos notificados que verifican la conformidad de los sistemas de IA con los estándares establecidos por la ley."
    
    elif texto == "Proceso Legislativo y Aplicación":
        return "La propuesta original de la Ley de Inteligencia Artificial fue presentada por la Comisión Europea en abril de 2021. La propuesta pasó por un proceso legislativo ordinario, incluyendo negociaciones entre el Parlamento Europeo, el Consejo de la Unión Europea y la Comisión Europea donde se llegó a un acuerdo en diciembre de 2023. El Reglamento de la Inteligencia Artificial fue finalmente adoptado en abril de 2024 y entró en vigor en junio de 2024.\n\n La aplicación de la Ley de Inteligencia Artificial es responsabilidad de los Estados miembros de la Unión Europea. La Comisión Europea tiene la responsabilidad de supervisar la aplicación de la ley y adoptar directrices técnicas. La Oficina Europea de Inteligencia Artificial juega un papel central en la coordinación y apoyo a los Estados miembros en la aplicación de la ley.\n\n La Ley de Inteligencia Artificial es un reglamento, lo que significa que es directamente aplicable en todos los Estados miembros de la Unión Europea. La ley establece un enfoque basado en el riesgo, lo que significa que los requisitos regulatorios varían según el nivel de riesgo que presenta un sistema de IA. La ley se basa en principios éticos como la seguridad, la transparencia, la rendición de cuentas y la no discriminación. La ley incluye disposiciones sobre gobernanza, como la creación de un Panel Científico de Expertos Independientes y un Foro Asesor. La ley establece mecanismos de aplicación como sanciones financieras e investigaciones de mercado.\n\n Plazos de Aplicación:\n\n  **6 meses después de la entrada en vigor (21 de diciembre de 2024)**\n\n Prohibición de las prácticas de IA de alto riesgo que sean inaceptables por razones de seguridad, protección de la salud pública, protección del medio ambiente o protección de los derechos y libertades fundamentales.\n\n **9 meses después de la entrada en vigor (21 de marzo de 2025)**\n\n Publicación de las listas de sistemas de IA de alto riesgo y de los requisitos específicos para cada categoría de sistema de IA de alto riesgo. \n\n**12 meses después de la entrada en vigor (21 de junio de 2025)**\n\n Obligaciones de gobernanza para los proveedores y usuarios de sistemas de IA, incluyendo la implementación de un sistema de gestión de riesgos y la designación de un responsable de conformidad.\n\n **18 meses después de la entrada en vigor (21 de diciembre de 2025)**\n\n Obligaciones de transparencia para los usuarios de sistemas de IA, incluyendo el derecho a ser informados sobre el uso de la IA y a tener la posibilidad de deshabilitar o desinstalar el sistema de IA.\n\n **36 meses después de la entrada en vigor (21 de junio de 2027)**\n\n Obligaciones para los sistemas de IA que son componentes de sistemas informáticos a gran escala establecidos por la legislación de la UE en los ámbitos de libertad, seguridad y justicia, como el Sistema de Información de Schengen."
    
    elif texto == "Reacciones y Críticas":
        return "**Impacto Global**\n\nSe espera que la ley tenga repercusiones a nivel internacional, afectando a empresas que deseen operar en Europa. Este marco regulador podría influir en la regulación de IA a nivel global. La AI Act puede establecer un punto de referencia para otras regiones del mundo que buscan regular la IA. Los altos estándares establecidos por la AI Act podrían impulsar a otros países a adoptar enfoques regulatorios similares, fomentando así la convergencia global en materia de regulación de la IA. Esto podría contribuir a crear un entorno global más seguro y responsable para el desarrollo y uso de la IA, beneficiando a todos los actores involucrados. La AI Act proporciona un marco claro y estable para las empresas que operan en el ámbito de la IA, lo que puede generar mayor confianza e inversión en el sector. Al establecer requisitos claros para la seguridad, la transparencia y la rendición de cuentas, la AI Act puede incentivar a las empresas a desarrollar sistemas de IA más responsables y éticos. Esto podría conducir a un aumento en la innovación en el sector de la IA, con el desarrollo de nuevas tecnologías y aplicaciones que beneficien a la sociedad en su conjunto.\n\nLa AI Act incorpora principios éticos clave en su diseño, como la protección de los derechos humanos, la no discriminación y la seguridad. Al establecer requisitos específicos para mitigar los riesgos potenciales de la IA, la AI Act puede ayudar a proteger los derechos y libertades fundamentales de las personas en el mundo digital. Esto podría contribuir a crear una sociedad más justa e inclusiva donde la IA se utiliza de manera responsable y beneficiosa para todos.\n\nLa Unión Europea se posiciona como un líder global en la regulación de la IA con la AI Act. Esto podría atraer a empresas e inversiones al bloque europeo, creando un ecosistema de innovación en IA próspero y competitivo. La AI Act también puede servir como herramienta para promover la cooperación internacional en materia de regulación de la IA, estableciendo estándares globales que beneficien a todos los países.\n\nLa implementación efectiva de la AI Act será crucial para lograr su impacto global deseado. Se requerirá la colaboración de gobiernos, empresas, academia y sociedad civil para garantizar que la ley se aplique de manera coherente y efectiva en toda la Unión Europea. También será importante abordar los posibles desafíos relacionados con la extraterritorialidad de la ley y su impacto en países fuera de la Unión Europea\n\n**Derechos Humanos**\n\n_Impactos positivos_\n\nProtección contra la discriminación: La AI Act prohíbe el uso de sistemas de IA que discriminen a las personas por motivos de raza, origen étnico, religión, género, orientación sexual, discapacidad u otros motivos protegidos por la ley. Esto puede ayudar a garantizar que todos los individuos sean tratados de manera justa e igualitaria, independientemente de sus características personales.\n\nPrivacidad y protección de datos: La AI Act establece requisitos estrictos para la recopilación, el uso y el almacenamiento de datos personales por parte de los sistemas de IA. Esto puede ayudar a proteger la privacidad de las personas y garantizar que sus datos personales se utilicen de manera responsable y ética.\n\nSeguridad y protección: La AI Act exige que los sistemas de IA se diseñen y desarrollen de manera segura para evitar daños a las personas o sus bienes. Esto puede ayudar a prevenir accidentes, lesiones y otros daños causados por sistemas de IA defectuosos o mal utilizados.\n\nTransparencia y rendición de cuentas: La AI Act exige que los sistemas de IA sean transparentes y explicables. Esto significa que las personas deben poder comprender cómo funcionan los sistemas de IA y cómo se toman las decisiones basadas en ellos. Esto puede ayudar a garantizar que las personas puedan ejercer sus derechos y impugnar las decisiones tomadas por sistemas de IA.\n\nEmpoderamiento y participación: La AI Act busca empoderar a las personas para que participen en el desarrollo y uso de la IA. Esto incluye la posibilidad de que las personas expresen sus opiniones sobre los sistemas de IA y de que sean consultadas en el proceso de toma de decisiones.\n\n_Impactos potenciales negativos_\n\nLimitación de la libertad de expresión: La AI Act podría utilizarse para restringir la libertad de expresión si se utiliza para censurar contenido o para silenciar a las voces disidentes.\n\nAmenaza a la autonomía individual: La IA podría utilizarse para tomar decisiones que afecten significativamente la vida de las personas sin su consentimiento o conocimiento. Esto podría plantear desafíos a la autonomía individual y al derecho a la autodeterminación.\n\nDesigualdad y discriminación algorítmica: Los sistemas de IA podrían perpetuar o amplificar las desigualdades existentes en la sociedad si no se diseñan y desarrollan cuidadosamente. Esto podría conducir a una mayor discriminación contra grupos vulnerables.\n\nVigilancia masiva y pérdida de privacidad: La IA podría utilizarse para la vigilancia masiva de las personas, lo que podría tener un impacto negativo en la privacidad y la libertad personal.\n\nFalta de transparencia y sesgos algorítmicos: Los sistemas de IA pueden ser opacos y difíciles de entender, lo que dificulta que las personas identifiquen y desafíen los sesgos algorítmicos que pueden conducir a decisiones discriminatorias.\n\nPor ejemplo, organizaciones como Amnesty International han criticado la ley por no prohibir completamente el reconocimiento facial en tiempo real y la exportación de tecnologías de IA que podrían violar los derechos humanos.\n\n**Competitividad**\n\nLa AI Act persigue objetivos nobles como la protección de los derechos y libertades fundamentales, la seguridad y la transparencia, su implementación podría generar algunos desafíos y problemas de competitividad para las empresas, especialmente para las pequeñas (startups) y medianas empresas (pymes) , que podrían verse desfavorecidas frente a sus contrapartes americanas y chinas debido a las nuevas regulaciones.\n\n_Costos de cumplimiento_\n\nLas empresas, especialmente las pymes, podrían enfrentar costos significativos para cumplir con los requisitos de la AI Act, incluyendo la evaluación de conformidad de sus sistemas de IA, la implementación de medidas de seguridad y protección de datos, y la documentación de sus procesos. Estos costos podrían ser especialmente gravosos para las pymes que no cuentan con los recursos financieros o técnicos necesarios para adaptarse a la nueva normativa.\n\n_Incertidumbre regulatoria_\n\nLa AI Act es una ley relativamente nueva y aún se están desarrollando las directrices técnicas y los procedimientos de evaluación de conformidad. Esta incertidumbre regulatoria podría dificultar que las empresas planifiquen sus inversiones y desarrollen nuevos productos y servicios de IA.\n\n_Falta de claridad sobre los requisitos específicos_\n\nLa AI Act establece un enfoque basado en el riesgo, lo que significa que los requisitos específicos varían según el nivel de riesgo que presenta un sistema de IA. Sin embargo, la definición de _riesgo_ y los criterios para determinar el nivel de riesgo de un sistema de IA aún no están completamente definidos. Esta falta de claridad podría generar dificultades para las empresas a la hora de determinar si sus sistemas de IA están sujetos a la AI Act y qué requisitos específicos deben cumplir.\n\n_Desventaja competitiva para las empresas europeas_\n\nLa AI Act es una normativa específica de la Unión Europea, mientras que otros países o regiones del mundo pueden tener enfoques regulatorios diferentes o menos estrictos para la IA. Esto podría poner en desventaja competitiva a las empresas europeas que operan en el mercado global, ya que podrían tener que cumplir con requisitos más costosos y complejos que sus competidores en otros países.\n\n_Dificultades para innovar_\n\nLa AI Act tiene como objetivo proteger los derechos y libertades fundamentales, lo que es fundamental. Sin embargo, algunos expertos han señalado que los requisitos de la ley podrían dificultar que las empresas innoven en el campo de la IA, ya que podrían ser demasiado restrictivos o desalentar el desarrollo de nuevas tecnologías."
    
    elif texto == "Conclusiones":
        return "La Ley de IA de la UE representa un paso significativo hacia la regulación integral de la inteligencia artificial, estableciendo un equilibrio entre la promoción de la innovación tecnológica y la protección de los derechos y la seguridad de los ciudadanos. Esta ley no solo tendrá un impacto significativo dentro de la UE, sino que también podría influir en las normativas globales sobre inteligencia artificial. Para más detalles, puedes consultar la versión completa y resumida de la ley en el sitio oficial del Acta de IA"
# Funciones para cada sub-aplicación
def home():
    st.markdown(
    """
    <style>
    .titulo {
        font-size: 40px;
        color: #ff6347;
        font-family: 'Courier New', Courier, monospace;
        text-align: center;
    }
    .centered {
            justify-content: center;
            align-items: center;
            text-align: center;
        }
    .btn {
            margin: 10px;
        }
    .background {
            background-image: url('https://th.bing.com/th/id/OIP.GQUyV1dFiPXuoUwzZ--zJgHaE8?rs=1&pid=ImgDetMain');
            background-size: cover;
            height: 100%;
            width: 100%;
            position: absolute;
            top: 0;
            left: 0;
            z-index: -1;
    }
    </style>
    """,
    unsafe_allow_html=True,
    )
    st.markdown("<div class='background'></div>", unsafe_allow_html=True)
    st.markdown('<p class="titulo">Regularizaciones</p>', unsafe_allow_html=True)
    st.image("https://th.bing.com/th/id/OIP.GQUyV1dFiPXuoUwzZ--zJgHaE8?rs=1&pid=ImgDetMain", caption="Descripción de la imagen")
    st.markdown("<div class='centered'>", unsafe_allow_html=True)
    if st.button("AI Act", key="btn1"):
        st.session_state.page = "sub_app_1"
    if st.button("RDA", key="btn2"):
        st.session_state.page = "sub_app_2"
    st.markdown("</div>", unsafe_allow_html=True)

def sub_app_1():

    if st.button("Regresar a la Página Principal"):
        st.session_state.page = "home"
    st.markdown(
    """
    <style>
    .titulo {
        font-size: 40px;
        color: #ff6347;
        font-family: 'Courier New', Courier, monospace;
        text-align: center;
    }
    .usuario {
        font-size: 14px;
        font-family: Arial, sans-serif;
        border: 2px dashed black;
        padding: 15px;
        border-radius: 5px;
    }
    .chatbot {
        font-size: 22px;
        color: #1e90ff;
        font-family: 'Comic Sans MS', cursive, sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True,
    )

    # verde: #4caf50
    # rojo: #ff6347

    st.markdown('<p class="titulo">LEY DE INTELIGENCIA ARTIFICIAL (IA) DE LA UE</p>', unsafe_allow_html=True)
    st.markdown('<p class="usuario">La Ley de Inteligencia Artificial (IA) de la Unión Europea, también conocida como AI Act, fue aprobada por el Parlamento Europeo en marzo de 2024. Esta ley busca establecer un marco regulador robusto para el uso y suministro de sistemas de IA dentro de la UE, marcando un precedente global en la regulación de tecnologías emergentes.</p>', unsafe_allow_html=True)
    st.write("¿Que información deseas obtener acerca de la IA Act?")


    botones_y_textos = {
        "Clasificación de Riesgos": textos("Clasificación de Riesgos"),
        "Nuevas Instituciones y Órganos": textos("Nuevas Instituciones y Órganos"),
        "Evaluación de la conformidad": textos("Evaluación de la conformidad"),
        "Proceso Legislativo y Aplicación": textos("Proceso Legislativo y Aplicación"),
        "Reacciones y Críticas": textos("Reacciones y Críticas"),
        "Conclusiones": textos("Conclusiones")
    }

    # Inicializar una variable para guardar el texto seleccionado
    texto_seleccionado = ""

    # Crear los botones y actualizar el texto seleccionado según el botón presionado
    for boton, texto in botones_y_textos.items():
        if st.button(boton):
            texto_seleccionado = texto

    # Mostrar el texto seleccionado en el cuerpo principal de la app
    if texto_seleccionado:
        st.write(texto_seleccionado)

    menu_items = {
        "Ley Completa": "https://www.europarl.europa.eu/doceo/document/TA-9-2024-0138-FNL-COR01_ES.pdf",
        "Recursos Legales": "https://eur-lex.europa.eu/homepage.html",
        "Law topic artificial intelligence": "https://www.europarl.europa.eu/news/en/press-room/20240308IPR19015/artificial-intelligence-act-meps-adopt-landmark-law",
        "European commission": "https://digital-strategy.ec.europa.eu/en/policies/artificial-intelligence",
        "Oficina europea de IA": "https://digital-strategy.ec.europa.eu/es/policies/ai-office",
        "EUR-Lex": "https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=celex%3A52021PC0206",
        "Preguntas y respuestas": "https://ec.europa.eu/commission/presscorner/api/files/document/print/es/qanda_21_1683/QANDA_21_1683_ES.pdf",
        "Commissioner for Human Rights": "https://www.coe.int/en/web/commissioner/thematic-work/digital-technologies",
        "Amnistia Internacional": "https://www.amnesty.org/es/latest/news/2023/06/eu-ai-act-at-risk-as-european-parliament-may-legitimize-abusive-technologies/",
        "Reglamento de IA": "https://www.consilium.europa.eu/es/press/press-releases/2023/12/09/artificial-intelligence-act-council-and-parliament-strike-a-deal-on-the-first-worldwide-rules-for-ai/",
        "Green light to  rules on AI": "https://www.consilium.europa.eu/en/press/press-releases/2024/05/21/artificial-intelligence-ai-act-council-gives-final-green-light-to-the-first-worldwide-rules-on-ai/pdf?trk=public_post_comment-text",
    }

    with st.sidebar:
        st.markdown('<p class="chatbot">REFERENCIAS</p>', unsafe_allow_html=True)
    # Crear botones dinámicamente y redirigir a la URL correspondiente
        for name, url in menu_items.items():
            if st.button(name):
                webbrowser.open_new_tab(url)
                # st.write(f"Redirigiendo a {url}...")
        
        st.image("IAimage.jpg", use_column_width=True)

def sub_app_2():
    st.title("Sub-Aplicación 2")
    st.write("Bienvenido a la Sub-Aplicación 2")
    if st.button("Regresar a la Página Principal"):
        st.session_state.page = "home"

# Inicialización de la sesión
if 'page' not in st.session_state:
    st.session_state.page = "home"

# Manejo de la navegación
if st.session_state.page == "home":
    home()
elif st.session_state.page == "sub_app_1":
    sub_app_1()
elif st.session_state.page == "sub_app_2":
    sub_app_2()
