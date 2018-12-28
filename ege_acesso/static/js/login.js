window.onload = function(){
    const l = document.location.pathname;
    if (l === '/ege/acesso/login/'){
        const username = document.getElementById("id_username");
        const password = document.getElementById("id_password");
        username.onblur = function () {
            if (username.value) { username.className += ' used'; }
        };
        password.onblur = function () {
            if (password.value) { password.className += ' used'; }
        };
    }
};