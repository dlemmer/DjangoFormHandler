function login() {
    var user = form.name.value;
    var password = form.sname.value;
    var mail = form.mail.value;

    if (user == "" & password == "" & mail == ""){
        alert("Пожалуйста, заполните поле формы!")
    } else {
        alert("Регистрация прошла успешно! Письмо отправлено на вашу электронную почту")
    }
}