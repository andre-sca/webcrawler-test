import logo from './logo.svg';
import './App.css';

import React from 'react'
import { ReactDOM } from 'react-dom';

const API_BASE_URL = 'http://localhost:5000/api/v1/'

class App extends React.Component {

  constructor(props) {
    super(props)
    this.state = {
      url: '',
      links: []
    }
  }

  getLinks = (event) => {
    event.preventDefault()
    fetch(API_BASE_URL + 'seeker', {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        url: this.state.url
      })
    })
    .then((response) => response.json())
    .then(linkList => {
      this.setState({
        links: linkList.result
      }, () => console.log(this.state.links))
    })
  }
  
  changeHandler = event => {
    this.setState({
      url: event.target.value
    })
  }



  render() {
    return(
      <>
        <form>
          <label>
            URL:
            <input type="text" value={this.state.url} onChange={this.changeHandler}></input>
          </label>
          <button onClick={this.getLinks}>Enviar</button>
        </form>
        <ul>
          {this.state.links.map((link) => (
            <li><a>{link}</a></li>
          ))}
        </ul>
      </>
    )
  }
}

export default App;
