import streamlit as st

def registration_page_interface() :
    '''Форма регистрации пользователя'''
    st.title("Регистрация пользователя")
    with st.form(key="registration_form") :
        st.markdown("Заполните поля")
        user_login = st.text_input("Введите логин")
        user_password = st.text_input("Введите пароль",type="password")
        submit_form = st.form_submit_button("Регистрация",use_container_width=True)

        if submit_form :
            return user_login,user_password,True
    return None,None,False