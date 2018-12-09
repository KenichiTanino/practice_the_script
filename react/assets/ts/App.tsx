import * as React from "react"
import * as ReactDOM from 'react-dom';
import { FormComponent } from "./components/react-form"
import { ClientTblPage } from "./components/react-table"
//import { Hello } from "./components/Hello"

import { BrowserRouter as AppRouter, Route, Link } from 'react-router-dom'

const liStyle = {
  display: 'inline',
  width: '100px'
}

const App = () => (
  <AppRouter>
     <div style={{width: '500px', textAlign: 'left'}}>
       <ul style={{display: 'flex'}}>
         <li style={liStyle}><Link to='/'>top</Link></li>
         <li style={liStyle}><Link to='/search'>search</Link></li>
       </ul>

       <div style={{marginLeft: '50px'}}>
         <Route exact path='/' component={Home} />
         <Route path='/search' component={Search} />
         <Route path='/new' component={New} />
       </div>
     </div>
  </AppRouter>
)

const Home = () => (
  <div>
    <h2>Home</h2>
    <p>Welcome to ようこそ</p>
    <p> 新規登録は　<Link to='/new'>こちら</Link></p>
    <p> 一覧は　<Link to='/search'>こちら</Link></p>
  </div>
)

const Search = () => (
  <div>
    <h2>検索 and 一覧</h2>
    <ClientTblPage />
  </div>
)

const New = () => (
  <div>
    <h2>登録</h2>
    <p>ここで登録します</p>
    <FormComponent name="" email="" />
  </div>
)

export default App
