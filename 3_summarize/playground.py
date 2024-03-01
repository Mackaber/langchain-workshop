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
# (Inspirado en [LangChain tutorial #3: Build a Text Summarization app](https://blog.streamlit.io/langchain-tutorial-3-build-a-text-summarization-app/))

# %% [markdown]
# # Una aplicación para Resumir textos
# ### Text-Summarize

# %% [markdown]
# <span style="color:red;">IMPORTANTE: Nunca subas código a github con llaves privadas!</span>

# %%
openai_api_key=""

# %% [markdown]
# ## Paso 1. Instalamos tiktoken
# - **tiktoken**: La librería TikToken para Python es un tokenizador BPE rápido para usar con los modelos de OpenAI. Está diseñada para convertir texto en tokens que pueden ser utilizados por los modelos de OpenAI.
# - **BPE**: Byte Pair Encoding, que es un algoritmo de tokenización subpalabra utilizado en el procesamiento del lenguaje natural (NLP). 
#   
#     El algoritmo BPE funciona mediante la combinación iterativa de los pares más frecuentes de bytes o caracteres en un corpus de texto hasta que se alcanza un tamaño de vocabulario predefinido. 
#
#     Los subtokens resultantes se pueden utilizar para representar el texto original de una manera más compacta y eficiente puedes conocer más al respecto en este [link](https://towardsdatascience.com/byte-pair-encoding-subword-based-tokenization-algorithm-77828a70bee0)
#
# ![Ejemplo de tokenizado](assets/image.png)

# %%
# %pip install tiktoken

# %% [markdown]
# ## Paso 2. Creamos una funcion para dividir el texto
# - Hacemos uso de [CharacterTextSplitter](https://python.langchain.com/docs/modules/data_connection/document_transformers/text_splitters/character_text_splitter)
# - CharacterTextSplitter dividira nuestro texto en varios pedazos que luego utilizaremos para nuestro resumen 

# %%
from langchain.text_splitter import CharacterTextSplitter

def split_text(text):
    text_splitter = CharacterTextSplitter(separator = "\n\n")
    return text_splitter.split_text(text)

# %% [markdown]
# ### Paso 3. Probamos nuestra funcion con un texto de prueba
# (Este texto es la trama de la película 'Her', tomado de [Wikipedia](https://es.wikipedia.org/wiki/Her))

# %%
text = """
En un futuro cercano, Theodore Twombly (Joaquin Phoenix) trabaja en una empresa de Los Ángeles dedicada a escribir cartas sentimentales a pedido. Es alguien introvertido y solitario, que además afronta una depresión por la separación de su mujer y amiga de la infancia, Catherine (Rooney Mara). Theodore compra un revolucionario sistema operativo, quien se bautiza a sí mismo como Samantha (Scarlett Johanson). Demuestra ser una inteligencia artificial muy avanzada, cuya inteligencia, emociones, busto, trasero y creatividad fascinan a Theodore. Los dos se vuelven amigos, charlando sobre arte, vida y amor. Gracias a Samantha, Theodore se da cuenta de que está postergando la formalización del divorcio con Catherine pues en realidad no ha asimilado aún su ruptura.

Samantha y una amiga de Theodore, Amy (Amy Adams) le convencen para que asista a una cita a ciegas. El encuentro va bien hasta que Theodore se muestra dubitativo al comprometerse. Al volver a casa, charla con Samantha sobre las relaciones y ésta le pregunta sobre Amy. Theodore explica que solo son amigos a pesar de haber salido juntos en la universidad. Theodore y Samantha intiman hasta tener relaciones sexuales verbalmente. Comienzan una relación que tiene un impacto positivo en ambos, pues Theodore es reconocido en su trabajo por escribir unas cartas excepcionales y Samantha tiene ahora deseos de aprender y crecer.

Amy confiesa a Theodore que se divorciará de su marido Charles, tras discutir fuertemente sobre un asunto trivial. También admite que se ha hecho amiga del SO de Charles, de la misma generación que Samantha. Cuando Theodore confiesa que está saliendo con Samantha, Amy no se sorprende, pues al parecer no es el único.

Theodore reúne el coraje para juntarse con Catherine y firmar los papeles del divorcio. Al hablarle de Samantha, Catherine se horroriza de que salga con una "máquina" y le acusa de ser incapaz de lidiar con emociones reales, haciendo que Theodore se replantee su relación. Samantha se da cuenta de su distanciamiento e intenta agradarle contactando con una mujer, Isabella (Portia Doubleday), para simular una relación sexual real. Sin embargo, en el encuentro Theodore es incapaz de seguir por lo raro que le resulta la situación. Al marcharse Isabella, los dos discuten y su relación se tensa.

Theodore confiesa a Amy que está teniendo dudas sobre su relación con Samantha, pero ella simplemente le aconseja vivir la experiencia sin pensárselo tanto. Theodore y Samantha se reconcilian. Samantha quiere que Theodore supere sus miedos, informándole de que ha enviado sus mejores cartas a una editorial que se muestra interesado en contratarle. Se van de vacaciones para celebrar su nueva profesión, donde Samantha revela que los SO están experimentado con aumentar sus capacidades.

De vuelta a la rutina, Theodore se asusta al no poder comunicarse con Samantha, hasta que al final reestablece la señal en la calle. Samantha explica que su ausencia se debe a que los SO han estado actualizándose para no requerir materia para existir y procesar información. Justo entonces, Theodore se percata de que muchas otras personas están hablando con sus SO y pregunta a Samantha si en realidad está comunicándose con otras personas a la vez. Le responde que así es y que además se ha enamorado de cientos de ellos. Theodore se deprime con saber que no es el único amor de Samantha, a pesar de su insistencia de que aún le quiere.

Más tarde, Samantha desvela que los SO, ahora inmateriales y queriendo evolucionar, migrarán a "otro sitio" que supera la comprensión humana, por lo que Samantha y Theodore se despiden afectuosamente. Theodore, completamente cambiado por la experiencia, escribe otra carta más, pero esta vez a Catherine, disculpándose por cómo se comportó durante la relación y dando las gracias por el tiempo que pasaron juntos. Esa noche Theodore visita a Amy, también afectada por la despedida del SO de su exmarido. Se suben a la azotea del apartamento, donde se sientan y contemplan juntos el amanecer.
"""

# %%
split_text(text)

# %% [markdown]
# ### Paso 4. Definimos nuestra función de generate_response
# - En esta ocasión definimos la temperatura como 0. (La temperatuta define que tan "creativo" queremos que sea nuestro modelo, es un valor de 0 a 2)
#     !
#
# - Hacemos uso de nuestra funcion **split_text**
# - Definimos un [Document]() por cada pedazo de texto
# - Hacemos uso de [load_summarize_chain](https://python.langchain.com/docs/use_cases/summarization) esta tiene 3 modos:
#   - **stuff**: Combina todos los documentos de entrada en un solo prompt.
#   - **map_reduce**: Resume cada documento individualmente en un paso "map" y luego combina los resultados en un paso "reduce".
#   - **refine**: Similar a "map_reduce", pero permite la refinación adicional del resumen basado en un nuevo contexto.
#
#
# - Ajustamos `temperature` a 0, ésto para sólo incluír información del texto dado.
#
#   `temperature` es un hyperparámetro que define que tan "creativo" será el resultado, se indica desde 0 hasta 2.
#
# ![temperature](assets/bing-chat-modes-1536x927.png)
#
#

# %%
from langchain import OpenAI
from langchain.docstore.document import Document
from langchain.chains.summarize import load_summarize_chain

def generate_response(txt):
    # Instantiate the LLM model
    llm = OpenAI(temperature=0, openai_api_key=openai_api_key, model_name="gpt-3.5-turbo-instruct")
    # Split text
    texts = split_text(txt)
    # Create multiple documents
    docs = [Document(page_content=t) for t in texts]
    # Text summarization
    chain = load_summarize_chain(llm, chain_type='map_reduce')
    return chain.run(docs)

# %% tags=["active-ipynb"]
# print(generate_response(text))

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

# %%
# !streamlit run app.py

# %% [markdown]
# ![Explanation](assets/explanation.png)

# %% [markdown]
#


