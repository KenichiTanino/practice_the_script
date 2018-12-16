import * as React from "react"
import * as ReactDOM from 'react-dom';

import 'isomorphic-fetch';
import ReactTable from 'react-table'

import { SearchTextForm } from './react-search-text'

let tableData = 
[
    {
        "id": 1,
        "client_name": "a.b.c.d",
        "status": 'aaa',
        "create_date": "2018/10/12",
    },
    {
        "id": 2,
        "client_name": "f.d.a.dd",
        "status": 'bbb',
        "create_date": "2018/10/19",
    },
    {
        "id": 3,
        "client_name": "f.d.a.dd",
        "status": 'bbb',
        "create_date": "2018/10/19",
    }
]

interface BaseClientEditComponentProps {
    rowData: object,
};

class BaseClientEditComponent extends React.Component<BaseClientEditComponentProps>{
    constructor(props) {
        super(props);
        this.editItem = this.editItem.bind(this);
    }
    editItem(){
        alert("edit " + this.props.rowData);
        console.log(this.props.rowData);
    }
    render () {
        return (	
            <td >	
                <input type="button" className="btn btn-warning" value="Edit" onClick={this.editItem}/>
            </td>
        );
    }
}

let tHead = [
    { accessor: "id", Header: "ID"},
    { accessor: "client_name", Header: "クライアント名"},
    { accessor: "status", Header: "状態"},
    { accessor: "create_date", Header: "作成日"},
    { Header: '詳細', maxWidth: 50, Cell: row => <BaseClientEditComponent rowData={row} /> }
];

interface SearchTableData {
	id: number;
    client_name: string;
    status: string;
    create_date: string;
};

interface SearchTableState {
    value: string;
	tableData: SearchTableData[];
};

export class SearchTable extends React.Component<{}, SearchTableState>{
    constructor(props) {
        super(props);
		var init_value = "";
        let init_value_el =  document.getElementById('search_init_search')
        if (init_value_el != null) {
			init_value = init_value_el.textContent;
		}
		
        this.state = {
			value: init_value,
			tableData: tableData
		};
        this.handleSubmit = this.handleSubmit.bind(this)
    }

    handleSubmit(value) {
        //window.alert('Inputted value: ' + value)
		const self = this;
		fetch('/api/table')
			.then(function(response) {
				if (response.status >= 400) {
					throw new Error("Bad response from server");
				}
				return response.json();
			})
			.then(function(tables) {
				console.log(tables);
            	self.setState({tableData: tables});
    		});
	}

    render () {
        return (
            <div>
                <SearchTextForm value={this.state.value} onSubmit={this.handleSubmit.bind(this)} />
            	<ReactTable data={this.state.tableData} columns={tHead} className="-striped -highlight" showPaginationBottom={false} />
            </div>
        );
    }
};
