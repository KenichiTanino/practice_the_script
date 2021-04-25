import * as React from "react"
import * as ReactDOM from 'react-dom';

export interface FormProps { name: string; email: string; };

export interface FormState {
	data: FormProps;
};

export interface event { name: string; email: string; };

export class FormComponent extends React.Component<FormProps, FormState>{
	constructor(props) {
		super(props);
		this.state = {
        	/// ネストされたオブジェクトを用意
            data: {
                name: '',
                email: ''
            }
        };
        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleChange = this.handleChange.bind(this);
    }

    handleChange(event: React.ChangeEvent<HTMLInputElement>) {
        // ネストされたオブジェクトのdataまでアクセスしておく
        var data = this.state.data;

        // eventが発火したname属性名ごとに値を処理
        switch (event.target.name) {
            case 'name':
                data.name = event.target.value;
                break;
            case 'email':
                data.email = event.target.value;
                break;
        }

        // 状態を更新
        this.setState({
            data: data
        });
    }

    handleSubmit() {
        console.log(this.state.data.name);
        console.log(this.state.data.email);
    }

    render() {
        return (
            <form action="" onSubmit={this.handleSubmit}>
                {/* Name */}
                <label htmlFor="name">お名前</label>
                <input type="text" name="name" value={this.state.data.name} onChange={this.handleChange} />

                {/* Email */}
                <label htmlFor="email">メールアドレス</label>
                <input type="email" name="email" value={this.state.data.email} onChange={this.handleChange} />

                 {/* Submit Button */}
                <button type="submit">送信</button>
            </form>
        );
    }
};
