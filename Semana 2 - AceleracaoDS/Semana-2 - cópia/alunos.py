import streamlit as st
import pandas as pd

def main():
    st.title('Hello world!')
    #st.header('This is a header')
    #st.subheader('This is a subheader')
    #st.text('This is a text')
    #st.subheader('Codenation logo')
 #   #st.image('logo.png')
 #   botao = st.button('Botao')
 #   if botao:
#        st.markdown('Clicado')
#    st.markdown('Checkbox')
#    check = st.checkbox('Checkbox')
#    if check:
#        st.markdown('Clidado')
#    st.markdown('Radio')
#    radio = st.radio('Escolha as opcoes', ('Opt 1', 'Opt 2'))
#    if radio == 'Opt 1':
#        st.markdown('Opcao 1')
#    if radio == 'Opt 2':
#        st.markdown('Opcao 2')
#    st.markdown('Select box')
#    select = st.selectbox('Choose opt', ('Opt 1', 'Opt 2'))
#    if select == 'Opt 1':
#        st.markdown('Opcao 1')
#    if select == 'Opt 2':
#       st.markdown('Opcao 2')
#    
#    st.markdown('multi')
#
#    multi = st.multiselect('Choose: ', ('Opt 1', 'Opt 2'))
#    if multi == 'Opt 1':
#        st.markdown('Opcao 1')
#    if multi == 'Opt 2':
#        st.markdown('Opcao 2')
#
#    st.markdown('File uploader')
#    file = st.file_uploader('Choose your file', type = 'csv')
#    if file is not None:
#        st.markdown('Nao esta vazio')

    file = st.file_uploader('Upload your file: ', type = 'csv')
    if file is not None:
        slider = st.slider('Valores', 1,100)
        df = pd.read_csv(file)
        st.dataframe(df.head(slider))
        st.markdown('TABELINHA')
        st.table(df.head(slider))

        st.write(df.columns)
        st.table(df.groupby('species')['petal_width'].mean())





if __name__ == '__main__':
    main()