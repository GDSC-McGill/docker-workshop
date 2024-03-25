
(async () => {
    console.log("fetching data from pyserver...")
    const resp = await fetch("http://pyserver:9999/data")
    console.log("data: ", await resp.text())
})()
