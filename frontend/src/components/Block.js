import React from 'react'

const Block = (props) => {
    const title = props.title
    return (
        <div className="block-flexbox-container">
            <div className="block-empty">EMPTY</div>
            <div className="block-stats">STATS HERE</div>
        </div>
    )
}

export default Block
