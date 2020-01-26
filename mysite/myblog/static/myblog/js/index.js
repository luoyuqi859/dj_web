new Vue({
    el:'#index',
    data:{
        topmenu: [],
        banner: [],
        userUi: false,
        loginBtn: true,
        loginType: false,
        username: '',
        password: ''
    },
    mounted(){
        this.getData()
    },
    methods:{
        getData:function(){
            var self = this
            reqwest({
                url: '/api/index',
                method: 'get',
                type: 'json',
                success: function(data){
                    self.topmenu = data.topmenu
                    self.banner = data.banner
                    if(data.loginType == "OK"){
                        self.loginType = true
                    }else{
                        self.loginType = false
                    }
                }
            })
        },
        userlogin:function(){
            var self = this
            reqwest({
                url: '/api/index',
                method: 'post',
                type: 'json',
                headers:{
                    "X-CSRFTOKEN":csrftoken
                },
                data:{
                    username: self.username,
                    password: self.password
                },
                success:function(data){
                    console.log(data)
                    if (data.loginType=='OK') {
                        self.userUi = false
                        self.loginType = true
                    }
                },
                error:function(err) {
                    console.log(err)                 
                }                
            })
        },
        showuserUi:function(){
            this.userUi = !this.userUi
        },
        toadmin:function () {
            window.location.href = '/lwebadmin'
        }
    }
})