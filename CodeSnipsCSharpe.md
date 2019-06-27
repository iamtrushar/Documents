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
