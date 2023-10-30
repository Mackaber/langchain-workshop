# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: tags,-all
#     custom_cell_magics: kql
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.11.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# (Inspirado en [LangChain tutorial #2: Build a blog outline generator app in 25 lines of code](https://blog.streamlit.io/langchain-tutorial-2-build-a-blog-outline-generator-app-in-25-lines-of-code/))

# %% [markdown]
# # Una aplicación para "aprender cualquier cosa"
# ### PromptTemplate-Prompt-Answer

# %% [markdown]
# <span style="color:red;">IMPORTANTE: Nunca subas código a github con llaves privadas!</span>

# %%
global openai_api_key
openai_api_key="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"

# %%
from langchain.text_splitter import CharacterTextSplitter

def split_text(text):
    text_splitter = CharacterTextSplitter(separator = "\n\n")
    return text_splitter.split_text(text)


# %%
text = """
En 2044, Joe, de 25 años, trabaja para un sindicato criminal de Kansas City como asesino o "looper". En el futuro, dos eventos notables son la aparición de individuos con habilidades telequinéticas leves que les permiten mover objetos pequeños como monedas u otros, sin que se haya encontrado alguna utilidad; el segundo que se sabe que en algún punto dentro de los próximos treinta años se inventará el viaje en el tiempo, siendo declarado tecnología ilegal.

Dado que los sistemas de rastreo en el futuro de 2074 han hecho casi imposible deshacerse de los cuerpos sin ser detectados, los sindicatos criminales envían a sus enemigos al pasado para ser ejecutados. Dirigidos por un hombre del futuro llamado Abe, los loopers reciben, matan y eliminan los cuerpos de las víctimas cuyos rostros están ocultos, recuperando lingotes de plata adheridos a sus cuerpos como pago. Para ocultar las conexiones con el sindicato, cualquier looper que sobreviva hasta 2074 es enviado de regreso y asesinado por su versión joven, lo que se conoce como "cerrar el ciclo"; estos objetivos se identifican con lingotes de oro en lugar de plata, lo que marca el final del contrato del looper y su retiro obligatorio del sindicato.

Seth, el amigo de Joe, viene a verlo después de no poder matar a su yo futuro. El viejo Seth escapó después de advertirle que en el futuro una persona llamada Rainmaker derrocó a los cinco jefes principales y ordenó cerrar todos los ciclos. Joe esconde a Seth a regañadientes en la caja fuerte del piso de su apartamento, pero luego revela su ubicación después de que Abe amenaza con confiscar la mitad de la plata guardada de Joe. Los "Gat Men", pistoleros de élite de Abe capturan al joven Seth y comienzan a cortar partes del cuerpo, estos efectos aparecen en el cuerpo del Viejo Seth; por lo que se presenta en el lugar donde es retenido su yo joven para ser asesinado por Kid Blue, uno de los Gat Men.

Cuando llega el próximo objetivo de Joe, resulta ser su ciclo, pero llega con el rostro descubierto y las manos desatadas, por lo que el viejo Joe lo deja inconsciente y escapa. Al regresar a su apartamento el joven Joe lo encuentra saqueado por los Gat Men, Joe pelea con Kid Blue, se cae por una escalera de incendios y se desmaya.

En otra línea de tiempo, Joe mató a su ciclo como estaba previsto, se mudó a Shanghai y se convirtió en sicario para financiar su adicción a las drogas y su vida salvaje. Finalmente, un día conoció a una mujer de la cual se enamoró y con la cual se casó después de que lo ayudó a reformarse y desintoxicarse. Siete años mas tarde, un viejo amigo y looper retirado lo llama para advertirle que Rainmaker se ha apoderado de los sindicatos y ha ordenado que todos los ciclos sean cerrados; tras esto, da a Joe tres números de serie que son indicios de la identidad de Rainmaker. A los poco minutos los Gat Men llegan a recoger a Joe para cerrar el ciclo y su esposa muere accidentalmente cuando intenta evitarlo. Tras acabar con sus captores, el Viejo Joe se envía de regreso al 2044, alterando su historia al evadir a Joe y escapar.

El viejo Joe experimenta vagos recuerdos de las acciones de Joe en el presente y se encuentra con su yo más joven en un restaurante; allí le explica que quiere salvar a su esposa matando a Rainmaker cuando era niño. Adquiere un mapa de una biblioteca local donde ha identificado tres domicilios relacionados con los números de serie que recibió en el futuro; sin embargo, el joven Joe no se muestra interesado y señala que su único objetivo es matarlo para cerrar su ciclo y enmendarse ante Abe. Al lugar llega Kid Blue y los Gat Men iniciando un tiroteo donde el joven Joe logra robar un trozo del mapa con una de las locaciones antes de que ambos logren huir por separado.

El joven Joe decide adelantarse y esperar a su otro yo y emboscarlo cuando vaya al lugar del mapa, por lo que llega hasta una granja donde vive una mujer llamada Sara con Cid, su hijo pequeño; mientras, Abe ordena que sus hombres peinen el área alrededor de la ciudad para atrapar al joven Joe y aplicar el mismo método que usaron con Seth. Sara reconoce el número de serie del mapa como la designación del lugar y día de nacimiento de Cid usado por el hospital donde dio a luz. Joe deduce que su otro yo planea matar a los tres niños nacidos en ese hospital el mismo día ya que no sabe cuál se convertirá en Rainmaker. Un Gat Man llamado Jesse llega a la granja, pero Cid, quien siente simpatía por Joe, lo ayuda a esconderse.

Pronto se hace evidente que la relación de Sara y Cid es tensa en muchos sentidos, ya que el niño no ve a la mujer como su madre y la actitud de ella oscila entre el cariño, la frustración y un anormal miedo a que el niño se vuelva violento. Esa noche, Sara y Joe tienen relaciones sexuales y ella revela que no solo tiene poderes telequinéticos ligeramente superiores al promedio sino también que en su juventud abandonó la granja para vivir una vida desenfrenada en la ciudad y cuando quedo embarazada le regaló su hijo a su hermana ya que deseaba responsabilidades hasta que hace poco ella falleció y Sara decidió regresar para hacerse cargo de Cid y la granja.

Por la mañana, Joe se despierta y encuentra a Jesse apuntando a Sara con una pistola. Cid atestigua esto y asustado libera un despliegue de poder psíquico que afecta a toda la casa, apenas dando tiempo a Sara de huir con Joe antes que el niño pierda el control y mate a Jesse de forma atroz. Al darse cuenta de que el niño es un psíquico poderoso como ningún otro que haya existido, Joe deduce que no solo es quien asesinó a la hermana de Sara durante una rabieta, ya que no tiene interés en aprender a controlar sus habilidades, sino también que es quien se convertirá en Rainmaker y que ahora que él lo sabe el Viejo Joe podrá recordar ese hecho.

Cuando intenta matar al segundo niño, Kid Blue captura al Viejo Joe y lo lleva con Abe, pero este se libera, mata a Abe y sus secuaces y va a la granja de Sara, seguido por Kid Blue. Mientras Joe mata a Kid Blue, el Viejo Joe persigue a Sara y Cid; cuando una bala roza la cara de Cid el niño pierde el control y desata una ola de poder que amenaza matar al anciano y a su madre, pero Sara finalmente logra calmarlo y motivarlo a controlar sus poderes antes de que pueda matar a alguien, posteriormente ordena a Cid huir por un campo de caña de azúcar mientras ella intenta demorar al Viejo Joe bloqueando su línea de fuego.

Joe tiene una epifanía y comprende que todo se trata de una paradoja: el viejo Joe matará a Sara pero no podrá evitar que Cid huya y crezca odiando a los loopers, por lo que al volverse adulto usará sus poderes para apoderarse de los sindicatos, exterminar a todos los loopers y con ello motivar al Viejo Joe a viajar al pasado. Sabiendo que Cid se convertirá en Rainmaker si el viejo Joe mata a Sara y viéndose incapaz de alcanzarlos para protegerla, el joven Joe se suicida, borrando así la existencia del Viejo Joe, salvando a Sara y evitando que Cid se convierta en Rainmaker.
"""

# %%
texts = split_text(text)

# %%
texts

# %%
from langchain.docstore.document import Document
docs = [Document(page_content=t) for t in texts]

# %%
docs[0]

# %%
from langchain import OpenAI
from langchain.docstore.document import Document
from langchain.chains.summarize import load_summarize_chain

def generate_response(txt):
    # Instantiate the LLM model
    llm = OpenAI(temperature=0, openai_api_key=openai_api_key)
    # Split text
    texts = split_text(txt)
    # Create multiple documents
    docs = [Document(page_content=t) for t in texts]
    # Text summarization
    chain = load_summarize_chain(llm, chain_type='map_reduce')
    return chain.run(docs)


# %% [markdown]
# ## Prompt templates:
#
# Un prompt template es una plantilla de texto que se utiliza para definir y componer funciones de inteligencia artificial (IA) en lenguaje natural. Estas plantillas se utilizan para crear prompts de lenguaje natural, generar respuestas, extraer información, invocar otros prompts o realizar cualquier otra tarea que pueda expresarse con texto
#
# Algunas características de los prompt templates son:
#
# - **Variables**: Se pueden incluir variables en las plantillas para que se inserten valores, funciones o variables en los prompts
# - **Llamadas a funciones externas**: Se pueden llamar a funciones externas desde las plantillas
# - **Pasaje de parámetros a funciones**: Se pueden pasar parámetros a las funciones desde las plantillas
#
# ![Template](assets/template.png)
#
# Algunos recursos:
#
# - [https://www.pinecone.io/learn/series/langchain/langchain-prompt-templates/](https://www.pinecone.io/learn/series/langchain/langchain-prompt-templates/)
# - [https://github.com/forReason/GPT-Prompt-Templates](https://github.com/forReason/GPT-Prompt-Templates)
# - [https://python.langchain.com/docs/modules/model_io/prompts/prompt_templates/](https://python.langchain.com/docs/modules/model_io/prompts/prompt_templates/)

# %% [markdown]
# ## Paso 1. Definamos un Template

# %%
template = """
  Como un profesor experto quiero que me propongas 
  una ruta de aprendizaje para aprender {topic}
"""

# %%
from langchain.llms import OpenAI
from langchain import PromptTemplate

def generate_response(topic):
  llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
  prompt = PromptTemplate(input_variables=['topic'], template=template)
  prompt_query = prompt.format(topic=topic)
  return llm(prompt_query)

# %% tags=["active-ipynb"]
# topic = """
#     Computación Cuántica
# """

# %% tags=["active-ipynb"]
# response = generate_response(topic)
# print(response)

# %% [markdown]
# ## Paso 4. Creamos nuestra app en Streamlit usando la funcion generate_response (Es casi idéntica a la de st_tutorial_1)
#
# - crea un nuevo archivo app.py
# - nuestra app hará uso de las funciones de streamlit:
#   - [st.title](https://docs.streamlit.io/library/api-reference/text/st.title)
#   - [st.form](https://docs.streamlit.io/library/api-reference/control-flow/st.form)
#   - [st.text_input](https://docs.streamlit.io/library/api-reference/widgets/st.text_input)
#   - [st.form_submit_button](https://docs.streamlit.io/library/api-reference/control-flow/st.form_submit_button)
#   - [st.info](https://docs.streamlit.io/library/api-reference/status/st.info)
#   - [st.warning](https://docs.streamlit.io/library/api-reference/status/st.warning)

# %% [markdown]
# ## Paso 5. Ejecuta la aplicación
# (También puedes ejecutarla ene una terminal aparte si así lo prefieres)

# %% language="bash"
# streamlit run app.py

# %% [markdown]
# ![Explanation](assets/explanation.png)

# %% [markdown]
#
