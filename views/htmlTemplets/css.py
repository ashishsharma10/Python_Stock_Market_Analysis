css = """
<style>
    body {
        background-color: #f0f0f0; /* Light gray background */
        color: #000000; /* Black text color */
        font-family: sans-serif; /* Sans-serif font */
    }

    .info-container{
        display: grid;
        grid-template-columns: auto auto auto;
    }
    
    .info-child{
        padding: 0.5rem;
        margin: 0.5rem;
        border-radius: 10px;
        border: 0.5px solid;
        display: flex;
        justify-content: space-between;
    }
    
    .info-child .value{
        font-weight: bold;
        font-size: large;
        margin: 0
    }
    
    .info-child .title{
        margin: 0
    }
</style>
"""