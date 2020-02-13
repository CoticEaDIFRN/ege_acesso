# SUAP-EaD Acesso



## Objetivo

Desenvolver e implantar um sistema de autenticação unificado que utilize o AD para as aplicações Web e Mobile Android que fazem parte do SUAP-EaD.


## Justificativa

Atualmente os usuários do EaD necessitam acessar vários serviços na web, para cada serviço é solicitado ao usuário que informe o IFRN-Id e a senha causando uma verdadeira proliferação de aplicativos que coletam e validam a senha. Este problema tente a aumentar pois estamos desenvolvendo uma série de aplicativos mobile (Android e iPhone).

Para se ter uma ideia de serviços ofertados via web ou mobile que os usuários do EaD consumem ou consumirão veja a Lista 1:

*Lista 1 - Serviços em uso ou a serem utilizados pelos usuários do Campus EaD*
1. Moodle acadêmico – Web
2. Moodle presencial – Web
3. Administração do portal do EaD – Web
4. Administração do portal do Colóquio – Web
5. Administração do portal do SEMEAD – Web
6. Central de chamados do EaD – Web
7. Ingresso – Web
8. Ecosistema de Gestão Educacional
8. Processo Seletivo – Web
9. Mensageiro instantâneo – Web, Android e iPhone, planejado



## Proposta

Desenvolver e implementar um Web Single Sign-On (W-SSO) e um Android Mobile Authenticator (AMA) para ser utilizado pelas aplicações cadastradas.

*Lista 2 -  Protocolos preferenciais*
1.	CAS
2.	OpenID
3.	SAML 1 e SAML2
4.	OAuth2
5.	**JWT**


### Requisitos

1.	O W-SSO deverá implementar ao menos o padrão **JWT**.
2.	O W-SSO deverá realizar o Web Single Log-Out (W-SLO) da sessão.
3.	O W-SSO opcionalmente implementará todos os serviços da Lista 2, em que utilizará o compartilhamento da sessão.
4.	Deverá permitir autenticação de serviços utilizando tokens de autenticação.
5.	Deverá permitir a invalidação de token e da sessão associada a este token.
6.	Deverá permitir a gestão do perfil do usuário.
7.	Deverá permitir que o usuário tenha mais de uma função institucional atribuída a sua identidade e que cada um esteja associado a uma UOrg., com período de início e fim devidamente definidos.
8.	Poderá usar como opções de W-SSO as implementações da lista Lista 2.


```bash

# using curl
curl -X GET http://localhost/sead/acesso/api/v1/users/?format=json -H 'Authorization: Secret _SUAP_EAD_ACESSO_JWT_SECRET_'


# using httpie
http --json http://localhost/sead/acesso/api/v1/users/  'Authorization:Secret _SUAP_EAD_ACESSO_JWT_SECRET_'

```