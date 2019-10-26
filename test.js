const graphrequest = require('graphql-request');
const query = `{
  gammaEvents(date:"2019-10-26", category:"Public") {
    ResName
    Category
    SubCategory
    ResDate
    StartTime
    EndTime
    Area
    ShowType
  }
}`
graphrequest.request('https://gammaql.gsc.org.uk/', query).then(data => console.log(data))

