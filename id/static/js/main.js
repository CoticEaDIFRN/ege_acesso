const page = new Vue({
    el: '#perfil',
    delimiters: ['${', '}'],

    data: {
        card_text: 'Lorem ipsum dolor sit amet, brute iriure accusata ne mea. Eos suavitate referrentur ad, te duo agam libris qualisque, utroque quaestio accommodare no qui. Et percipit laboramus usu, no invidunt verterem nominati mel. Dolorem ancillae an mei, ut putant invenire splendide mel, ea nec propriae adipisci. Ignota salutandi accusamus in sed, et per malis fuisset, qui id ludus appareat.',
        photo_user: 'https://cdn3.iconfinder.com/data/icons/black-easy/512/538642-user_512x512.png',
        edit_buttons: true,
        dialog_bio: false,
        dialog_email: false,
        switch_email: false,
        switch_needs: true,
        options_needs: false,
        selected: [],
        biografy: '',
        email: [],
        special_needs_visao: [
            'Cegueira',
            'Baixa visão',
            'Daltonismo',
            'Fotofobia'
        ],
        special_needs_audicao: [
            'Surdez total',
            'Perda auditiva'
        ],
        special_needs_outras: [
            'Autismo',
            'Doença crônica',
            'Deficiência de aprendizado',
            'Doença mental',
            'Deficiência física',
            'Distúrbios da fala e da linguagem',
            'Perda de memória',
        ],
        recursos: null,
        cursos: [
            {
                nome: 'Tecnologia e Desenvolvimento de Software',
                codigo: '0000.0000.000-00',
                media: 7.0,
                aproveitamento: 70
            },
            {
                nome: 'Matemática financeira',
                codigo: '0000.0000.000-00',
                media: 5.0,
                aproveitamento: 50
            },
            {
                nome: 'Gestão Ambiental',
                codigo: '0000.0000.000-00',
                media: null,
                aproveitamento: 20
            }
        ],
        color_bar: []
    },
    created () {
        for (let i = 0; i <= this.cursos.length - 1; i++) {
            if (this.cursos[i].aproveitamento >= 70) { this.color_bar[i] = "success" }
            else if (this.cursos[i].aproveitamento >= 30 && this.cursos[i].aproveitamento < 70) { this.color_bar[i] = "warning" }
            else this.color_bar[i] = "error"
        }
        let rec = document.cookie.slice(document.cookie.indexOf("=")+1, document.cookie.indexOf(";"));
        let rec2 = document.cookie.indexOf("bvisao=")+1;
        // this.hide_conf = (rec === 'true');
        console.log(document.cookie, rec, rec2);

        let sead_user = JSON.parse(document.getElementById('perfil').dataset.content);
        console.log(sead_user);

        axios({
          method: 'get',
          url: `../id/api/v1/users/${sead_user}`
        })
        .then(response => {
            this.biografy = response.data.biografy;
            this.email = [
                {tipo: 'pessoal', data: response.data.email},
                {tipo: 'corporativo', data: response.data.enterprise_email},
                {tipo: 'academico', data: response.data.academic_email},
                {tipo: 'escolar', data: response.data.scholar_email}
            ];
            console.log(response.data)
        })
        .catch(error => console.log('put error:', error))
    },
    // hide_config=true; recurso_bvisao=true; recurso_leg=true; recurso_cfcor=true; csrftoken=BZNgFGO7YVzjNbT9hQumgAB34TdL3HvOsrR2b1ET39J1MQdw2oKUQumFDj69fBsH
    methods: {
        save_bio: function () {
            this.dialog_bio = false;

            axios({
              method: 'post',
              url: './biografy/',
              data: {biografy: document.getElementById('bio').value},
            })
            .then(response => {
              console.log(response)
            })
            .catch(error => console.log('put error:', error))
        },
        save_email: function () {
            this.dialog_email = false;

            axios({
              method: 'post',
              url: './email/',
              data: [
                  {email: document.getElementById(`${this.email[0].tipo}`)},
                  {enterprise_email: document.getElementById(`${this.email[1].tipo}`)},
                  {academic_email: document.getElementById(`${this.email[2].tipo}`)},
                  {scholar_email: document.getElementById(`${this.email[3].tipo}`)}
              ],
            })
            .then(response => {
              console.log(response)
            })
            .catch(error => console.log('put error:', error))
        },
        edit_recursos: function () {
            // axios({
            //   method: 'post',
            //   url: '/sead/perfil/acessibilidade',
            //   data: {painel_1: false}
            // })
            // .then(response => {
            //       console.log(response)
            //   })
            //     .catch(error => console.log('put error:', error))
            window.location.href = "/sead/perfil/acessibilidade?painel_1=false"
        }
    }
});

// Vue.component('button_edit', {
//     template: '<v-btn flat small color="white" v-on:click="show_edit_buttons">Editar dados</v-btn>',
//     methods: {
//         show_edit_buttons: function () {
//             page.edit_buttons = !page.edit_buttons
//         }
//     }
// });
