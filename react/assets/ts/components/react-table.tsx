import * as React from "react"
import * as ReactDOM from 'react-dom';

import 'isomorphic-fetch';
import { useTable } from 'react-table';
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
];

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
        alert("edit " + this.props.rowData['row']['client_name']);
        console.log(this.props.rowData);
    }
    render () {
      return (	
        <input type="button" className="btn btn-warning" value="Edit" onClick={this.editItem} />
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

function ReactTable({ columns, data }) {
  const {
    getTableProps,
    getTableBodyProps,
    headerGroups,
    rows,
    prepareRow,
  } = useTable<SearchTableData>({
    columns,
    data,
  })

  // Render the UI for your table
  return (
    <table {...getTableProps()}>
      <thead>
        {headerGroups.map(headerGroup => (
          <tr {...headerGroup.getHeaderGroupProps()}>
            {headerGroup.headers.map(column => (
              <th {...column.getHeaderProps()}>{column.render('Header')}</th>
            ))}
          </tr>
        ))}
      </thead>
      <tbody {...getTableBodyProps()}>
        {rows.map((row, i) => {
          prepareRow(row)
          return (
            <tr {...row.getRowProps()}>
              {row.cells.map(cell => {
                return <td {...cell.getCellProps()}>{cell.render('Cell')}</td>
              })}
            </tr>
          )
        })}
      </tbody>
    </table>
  )
}

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
            	<ReactTable data={this.state.tableData} columns={tHead} />
            </div>
        );
    }
};
