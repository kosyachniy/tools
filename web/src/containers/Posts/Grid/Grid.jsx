import React, { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import { withTranslation } from 'react-i18next'

import api from '../../../lib/api'

import Card from '../../../components/Card'


const Grid = (props) => {
    const {
        system, posts,
        postsGet,
    } = props

    const [loaded, setLoaded] = useState(null)

    const getPost = (data={}) => {
        api('posts.get', data).then(res => {
            postsGet(res['posts'])
        })
    }

    useEffect(() => {
        if (
            system.search !== loaded
            && (
                system.search === ''
                || system.search.length >= 3
            )
        ) {
            setLoaded(system.search)
            getPost({search: system.search})
        }
    })

    return (
        <>
            <div className="album py-2">
                <div className="row">
                    { posts.map((el, num) =>
                        <Card post={ el } key={ num } />
                    ) }
                </div>
            </div>
        </>
    )
}

export default withTranslation()(Grid);
