import streamlit as st
import pandas as pd

from db_fxn import (create_table, add_data, delete_data, view_all_data, view_unique_words, get_word, 
    edit_word_data, delete_data, select_word) 

def main():
    st.markdown('## Good Word in Business')
    menu = ['Today', 'Create', 'Read', 'Update', 'Delete', 'About']
    choice = st.sidebar.selectbox('Menu', menu)

    link = '[home](http://linkprivate.s3-website-ap-northeast-1.amazonaws.com/)'
    st.sidebar.markdown(link, unsafe_allow_html=True)
    st.sidebar.caption('homeに戻る')

    create_table()

    if choice == 'Today':
        if st.button('View Word of today'):
            result = select_word()
            # st.write(result)
            value = result[0][0]
            st.write(value)

    elif choice == 'Create':
        st.markdown('#### Add Item')

        word = st.text_area('good word')
        if st.button('Add Word'):
            add_data(word)
            st.success('Successfully Add Word:{}'.format(word))

    elif choice == 'Read':
        st.markdown('#### View Items')
        result = view_all_data()
        # st.write(result)
        df = pd.DataFrame(result, columns=['word'])
        with st.expander('View All Data'):
            st.dataframe(df)

    elif choice == 'Update':
        st.markdown('#### Edit / Update Items')
        result = view_all_data()
        # st.write(result)
        df = pd.DataFrame(result, columns=['word'])
        with st.expander('Current Data'):
            st.dataframe(df)

        # st.write(view_unique_words())
        list_of_word = [i[0] for i in view_unique_words()] # dict型から値のみ取り出す
        # st.write(list_of_word)

        selected_word = st.selectbox('Word To Edit', list_of_word)

        selected_result = get_word(selected_word)
        st.write(selected_word)

        if selected_result:
            word = selected_result[0][0] # [0]最初のindex　[0] value
            new_word = st.text_area('good word', word)
        if st.button('Update Word'):
            edit_word_data(new_word, word)
            st.success('Successfully Updated')
        
        result2 = view_all_data()
        df2 = pd.DataFrame(result2, columns=['word'])
        with st.expander('Updated Data'):
            st.dataframe(df2)        

    elif choice == 'Delete':
        st.markdown('#### Delete item')
        result = view_all_data()
        df = pd.DataFrame(result, columns=['word'])
        with st.expander('Current Data'):
            st.dataframe(df)

        list_of_word = [i[0] for i in view_unique_words()] # dict型から値のみ取り出す
        selected_word = st.selectbox('Word To Delete', list_of_word)
        st.warning('Do you want to delete : {}'.format(selected_word))
        if st.button('Delete Word'):
            delete_data(selected_word)
            st.success('Word has been Successfully Delete')

        new_result = view_all_data()
        df2 = pd.DataFrame(new_result, columns=['word'])
        with st.expander('Updated Data'):
            st.dataframe(df2)      

    else:
        st.markdown('#### About')               

if __name__ == '__main__':
    main()