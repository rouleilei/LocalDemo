webpackJsonp([1],{"75l9":function(e,t){e.exports={name:"axios",version:"0.21.4",description:"Promise based HTTP client for the browser and node.js",main:"index.js",scripts:{test:"grunt test",start:"node ./sandbox/server.js",build:"NODE_ENV=production grunt build",preversion:"npm test",version:"npm run build && grunt version && git add -A dist && git add CHANGELOG.md bower.json package.json",postversion:"git push && git push --tags",examples:"node ./examples/server.js",coveralls:"cat coverage/lcov.info | ./node_modules/coveralls/bin/coveralls.js",fix:"eslint --fix lib/**/*.js"},repository:{type:"git",url:"https://github.com/axios/axios.git"},keywords:["xhr","http","ajax","promise","node"],author:"Matt Zabriskie",license:"MIT",bugs:{url:"https://github.com/axios/axios/issues"},homepage:"https://axios-http.com",devDependencies:{coveralls:"^3.0.0","es6-promise":"^4.2.4",grunt:"^1.3.0","grunt-banner":"^0.6.0","grunt-cli":"^1.2.0","grunt-contrib-clean":"^1.1.0","grunt-contrib-watch":"^1.0.0","grunt-eslint":"^23.0.0","grunt-karma":"^4.0.0","grunt-mocha-test":"^0.13.3","grunt-ts":"^6.0.0-beta.19","grunt-webpack":"^4.0.2","istanbul-instrumenter-loader":"^1.0.0","jasmine-core":"^2.4.1",karma:"^6.3.2","karma-chrome-launcher":"^3.1.0","karma-firefox-launcher":"^2.1.0","karma-jasmine":"^1.1.1","karma-jasmine-ajax":"^0.1.13","karma-safari-launcher":"^1.0.0","karma-sauce-launcher":"^4.3.6","karma-sinon":"^1.0.5","karma-sourcemap-loader":"^0.3.8","karma-webpack":"^4.0.2","load-grunt-tasks":"^3.5.2",minimist:"^1.2.0",mocha:"^8.2.1",sinon:"^4.5.0","terser-webpack-plugin":"^4.2.3",typescript:"^4.0.5","url-search-params":"^0.10.0",webpack:"^4.44.2","webpack-dev-server":"^3.11.0"},browser:{"./lib/adapters/http.js":"./lib/adapters/xhr.js"},jsdelivr:"dist/axios.min.js",unpkg:"dist/axios.min.js",typings:"./index.d.ts",dependencies:{"follow-redirects":"^1.14.0"},bundlesize:[{path:"./dist/axios.min.js",threshold:"5kB"}]}},NHnr:function(e,t,a){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var s=a("7+uW"),n={render:function(){var e=this.$createElement,t=this._self._c||e;return t("div",{attrs:{id:"app"}},[t("router-view")],1)},staticRenderFns:[]};var r=a("VU/8")({name:"App"},n,!1,function(e){a("zVsq")},null,null).exports,o=a("/ocq");var i=null,l={name:"Login",data:function(){return{loginForm:{username:"admin",password:"111111"},loginRules:{username:[{required:!0,trigger:"blur",validator:function(e,t,a){a()}}],password:[{required:!0,trigger:"blur",validator:function(e,t,a){t.length<6?a(new Error("The password can not be less than 6 digits")):a()}}]},loading:!1,passwordType:"password",redirect:void 0}},mounted:function(){console.log("auto"),this.$http.get("/user/gen_captcha").then(function(e){i=e.data,document.getElementById("my_captcha").setAttribute("src","/user/get_captcha?code_id="+e.data)})},watch:{$route:{handler:function(e){this.redirect=e.query&&e.query.redirect},immediate:!0}},methods:{showPwd:function(){var e=this;"password"===this.passwordType?this.passwordType="":this.passwordType="password",this.$nextTick(function(){e.$refs.password.focus()})},handleLogin:function(){var e=this;this.$refs.loginForm.validate(function(t){if(!t)return console.log("error submit!!"),!1;console.log("oops"),console.log(i),e.loading=!0,e.$http.post("user/login?captcha="+e.loginForm.captcha+"&code_id="+i,e.loginForm).then(function(){e.$router.push({path:e.redirect||"/"}),e.loading=!1}).catch(function(){e.loading=!1})})}}},c={render:function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",{staticClass:"login-container"},[a("el-form",{ref:"loginForm",staticClass:"login-form",attrs:{model:e.loginForm,rules:e.loginRules,"auto-complete":"on","label-position":"left"}},[a("div",{staticClass:"title-container"},[a("h3",{staticClass:"title"},[e._v("Login Form")])]),e._v(" "),a("el-form-item",{attrs:{prop:"username"}},[a("span",{staticClass:"svg-container"},[a("svg-icon",{attrs:{"icon-class":"user"}})],1),e._v(" "),a("el-input",{ref:"username",attrs:{placeholder:"Username",type:"text",tabindex:"1","auto-complete":"on"},model:{value:e.loginForm.username,callback:function(t){e.$set(e.loginForm,"username",t)},expression:"loginForm.username"}})],1),e._v(" "),a("el-form-item",{attrs:{prop:"password"}},[a("span",{staticClass:"svg-container"},[a("svg-icon",{attrs:{"icon-class":"password"}})],1),e._v(" "),a("el-input",{key:e.passwordType,ref:"password",attrs:{type:e.passwordType,placeholder:"Password",tabindex:"2","auto-complete":"on"},nativeOn:{keyup:function(t){return!t.type.indexOf("key")&&e._k(t.keyCode,"enter",13,t.key,"Enter")?null:e.handleLogin.apply(null,arguments)}},model:{value:e.loginForm.password,callback:function(t){e.$set(e.loginForm,"password",t)},expression:"loginForm.password"}}),e._v(" "),a("span",{staticClass:"show-pwd",on:{click:e.showPwd}},[a("svg-icon",{attrs:{"icon-class":"password"===e.passwordType?"eye":"eye-open"}})],1)],1),e._v(" "),a("el-form",[a("el-input",{ref:"auth",attrs:{placeholder:"please input captcha",type:"text",tabindex:"1","auto-complete":"on"},model:{value:e.loginForm.captcha,callback:function(t){e.$set(e.loginForm,"captcha",t)},expression:"loginForm.captcha"}}),e._v(" "),a("img",{attrs:{id:"my_captcha"}})],1),e._v(" "),a("el-button",{staticStyle:{width:"100%","margin-bottom":"30px"},attrs:{loading:e.loading,type:"primary"},nativeOn:{click:function(t){return t.preventDefault(),e.handleLogin.apply(null,arguments)}}},[e._v("Login")])],1)],1)},staticRenderFns:[]},p=a("VU/8")(l,c,!1,null,null,null).exports;s.default.use(o.a);var u=new o.a({routes:[{path:"/",name:"HelloWorld",component:p}]}),d=a("zL8q"),m=a.n(d),g=a("mtWM"),h=a.n(g),f=a("aLYK");s.default.config.productionTip=!1,s.default.use(m.a),s.default.use(f.a,h.a),h.a.defaults.baseURL="http://127.0.0.1:9090",new s.default({el:"#app",router:u,components:{App:r},template:"<App/>"})},zVsq:function(e,t){}},["NHnr"]);
//# sourceMappingURL=app.171ecaf31d5de0f22217.js.map