How to use the model?

Because this is an LSTM model, when using this model, it should not be predictions = model(inputs)
The initial hidden layer of LSTM should be obtained first, and input into the model together with the input data like output, _ = model(inputs, initial_layer)