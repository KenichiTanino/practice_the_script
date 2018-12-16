import * as React from "react"
import * as ReactDOM from 'react-dom';

interface SearchTextFromProps {
    value: string;
    onSubmit: (value: string) => void;
};

interface SearchTextFromState {
    value: string;
};

export class SearchTextForm extends React.Component<SearchTextFromProps, SearchTextFromState> {
  constructor (props) {
    super(props);
    this.state = {value: this.props.value};
  }

  update (e) {
    console.log(e);
    this.setState({value: e.target.value})
  }

  submit (e) {
 	//window.alert('Inputted value: ' + this.state.value)
   	this.props.onSubmit(this.state.value)
    e.preventDefault()
  }

  render () {
    return (
      <form onSubmit={e => this.submit(e)} >
        <input type='text' value={this.state.value} onChange={e => this.update(e)} />
        <input type='submit' value='検索' />
      </form>
    )
  }
}
