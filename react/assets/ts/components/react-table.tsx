import * as React from "react"
import * as ReactDOM from 'react-dom';

import SortableTbl from 'react-sort-search-table';
//require.context('reactSortSearchTblFonts', true, /\.?/);

let MyData = 
[
    {
        "id": "1",
        "client_name": "a.b.c.d",
        "status": 'aaa',
        "create_date": "2018/10/12",
    },
    {
        "id": "2",
        "client_name": "f.d.a.dd",
        "status": 'bbb',
        "create_date": "2018/10/19",
    },
    {
        "id": "2",
        "client_name": "f.d.a.dd",
        "status": 'bbb',
        "create_date": "2018/10/19",
    }
]

interface BaseClientEditComponentProps {
    rowData: object,
    tdData: string,
};


class BaseClientEditComponent extends React.Component<BaseClientEditComponentProps>{
    constructor(props) {
        super(props);
        this.editItem = this.editItem.bind(this);
    }
    editItem(){
        alert("edit " + this.props.rowData);
        console.log(this.props.rowData, this.props.tdData);
    }
    render () {
        return (	
            <td >	
                <input type="button" className="btn btn-warning" value="Edit" onClick={this.editItem}/>
            </td>
        );
    }
}

export const ClientTblPage = (props) =>{
    let col = [
        "id",
        "client_name",
        "status",
        "create_date",
        "detail"
    ];
    let tHead = [
        "ID",
        "クライアント名",
        "状態",
        "作成日",
        "詳細"		
    ];
    let paging = false;
    let defaultCSS = false;
 
    return (
        <SortableTbl tblData={MyData} 
            paging={paging}
            defaultCSS={defaultCSS}
            tHead={tHead}
            customTd={[
                        {custd: BaseClientEditComponent, keyItem: "detail"},
                        ]}
            dKey={col}
        />
    );
};
 
ClientTblPage.propTypes = {
};
 
 
//ReactDOM.render(<ClientTblPage/>, document.getElementById("app"));
