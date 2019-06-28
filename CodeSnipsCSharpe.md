Pli validation example
```
var distanceResult = this
    .txtDistance.Text
    .As<decimal>(failMessage: "Please enter a number for distance to the next point.")
    .Where(distance => distance > 0m, "The distance must be greater than 0.");
if (distanceResult.IsFailure)
{
    // do translation and show error
    return;
}

var distance = (double)distanceResult.Unwrap();
...
```

Parse the JSON returned and assert that the members are as expected, i.e. something like:

var reportUrlResponse = WebMapsAccess.GetReportUrl(...);
var reportUrlJson = jsonSerializer.Parse<object>(reportUrlResponse);
Assert.AreEqual(true, reportUrlJson.GetProperty("success"));
Assert.AreEqual(string.Empty, reportUrlJson.GetProperty("message"));
Assert.AreEqual(
    "http://localhost/Reports/views/viewerah.aspx?...",
    reportUrlJson.GetProperty("value"));
