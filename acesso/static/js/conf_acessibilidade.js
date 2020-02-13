const data = new Vue({
    el: '#acessibilidade',
    delimiters: ['${', '}'],

    data: {
        painel_1: true,
        checkbox: true,
        rec_baixa_visao: false,
        rec_legendagem: false,
        rec_config_cor: false,
    },
    created () {
        let url = new URL(window.location.href);
        if (url.searchParams.get("painel_1")) {
            this.painel_1 = false
        }
    },
    updated () {
    },
    methods: {
        create_cookie (name, value) {
            let d = new Date();
            let year = d.getFullYear();
            year += 1;
            d.setFullYear(year);
            let utc = d.toUTCString().replace("GMT", "UTC");
            document.cookie = `${name}=${value}; expires=${utc}`;
        },
        avancar: function (switch_painel1) {
            console.log(switch_painel1);
            switch(switch_painel1) {
                case "libras":
                    alert('LIBRAS');
                    // code block
                    break;
                case "ledor":
                    alert('ledor');
                    // code block
                    break;
                case "outro":
                    alert('outro');
                    // this.create_cookie('hide_config', true);
                    // this.create_cookie('recurso_bvisao', this.rec_baixa_visao);
                    // this.create_cookie('recurso_leg', this.rec_legendagem);
                    // this.create_cookie('recurso_cfcor', this.rec_config_cor);
                    // window.location.href = "/sead/perfil/";
                    break;
                // default:
                //     this.painel_1 = !this.painel_1;
                //     break;
            }
        }
    },
});
