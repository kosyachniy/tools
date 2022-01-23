import React, { useState, useEffect } from 'react'
import { withTranslation } from 'react-i18next'

import api from '../../../lib/api'


const Curl = () => {
    const [method, setMethod] = useState('GET')
    const [url, setUrl] = useState('')
    const [data, setData] = useState('')
    const [headers, setHeaders] = useState([['Content-Type', 'application/json']])

    return (
        <>
            <div className="input-group w-50 pt-3 mb-3">
                <select
                    id="inputGroupSelect02"
                    className="form-select u-cursor"
                    aria-label="Default select example"
                    onChange={(event) => {setMethod(event.target.value)}}
                >
                    <option value="GET" defaultValue>GET</option>
                    <option value="POST">POST</option>
                    <option value="PUT">PUT</option>
                    <option value="DELETE">DELETE</option>
                    <option value="HEAD">HEAD</option>
                    <option value="OPTIONS">OPTIONS</option>
                    <option value="CONNECT">CONNECT</option>
                    <option value="TRACE">TRACE</option>
                    <option value="PATCH">PATCH</option>
                </select>
                <input
                    type="text"
                    className="form-control w-50"
                    placeholder="https://exaple.com/"
                    value={url}
                    onChange={(event) => {setUrl(event.target.value)}}
                />
            </div>
            <textarea
                id="exampleFormControlTextarea1"
                className="form-control w-50 mb-3"
                rows="3"
                placeholder='{"foo": "bar"}'
                onChange={(event) => {setData(event.target.value)}}
            >
                { data }
            </textarea>
            {
                headers.map((el, i) =>
                    <div className="input-group w-50 mb-3" key={i}>
                        <button
                            type="button"
                            id="button-addon1"
                            className="btn btn-danger"
                            onClick={() => {
                                setHeaders([
                                    ...headers.slice(0, i),
                                    ...headers.slice(i+1, headers.length,
                                )])
                            }}
                        >
                            <i className="fa fa-times" aria-hidden="true" />
                        </button>
                        <input
                            type="text"
                            className="form-control"
                            placeholder="HeaderName"
                            aria-label="Example text with button addon"
                            aria-describedby="button-addon1"
                            value={el[0]}
                            onChange={(event) => {
                                setHeaders([
                                    ...headers.slice(0, i),
                                    [event.target.value, el[1]],
                                    ...headers.slice(i+1, headers.length),
                                ])
                            }}
                        />
                        <input
                            type="text"
                            className="form-control"
                            placeholder="HeaderContent"
                            aria-label="Example text with button addon"
                            aria-describedby="button-addon1"
                            value={el[1]}
                            onChange={(event) => {
                                setHeaders([
                                    ...headers.slice(0, i),
                                    [el[0], event.target.value],
                                    ...headers.slice(i+1, headers.length),
                                ])
                            }}
                        />
                    </div>
                )
            }
            <button
                type="button"
                className="btn btn-outline-success w-50 mb-3"
                onClick={ () => {setHeaders([...headers, ['', '']])} }
            >
                + Header
            </button>
            <div className="container-fluid px-4">
                <div className="row w-50 gx-5">
                    <div className="col">
                        <button
                            type="button"
                            className="btn btn-success w-100"
                        >
                            Run
                        </button>
                    </div>
                    <div className="col">
                        <button
                            type="button"
                            className="btn btn-success w-100"
                        >
                            Convert to cURL
                        </button>
                    </div>
                </div>
            </div>
        </>
    )
}

export default withTranslation()(Curl);
