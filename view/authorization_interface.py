import streamlit as st

def authorization_page_interface() :
    '''Форма авторизации пользователя'''
    st.title("Авторизация пользователя")
    with st.form(key="authorization_form") :
        st.markdown("Заполните поля")
        user_login = st.text_input("Введите логин")
        user_password = st.text_input("Введите пароль",type="password")
        submit_form = st.form_submit_button("Войти",use_container_width=True)

        if submit_form :
            return user_login,user_password,True
    return None,None,False