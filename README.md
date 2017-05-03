## (Mostly Binary) encoder

Inspired by http://www.willmcginnis.com/2015/11/29/beyond-one-hot-an-exploration-of-categorical-variables/

### Setup categorical_encoder package
```
    $ python setup.py install
```

### Usage

For a full categorical dataset:
```python
from categorical_encoder.encoder_service import EncoderService
encoder_service = EncoderService(encoder_type='binary')
print encoder_service.fit_transform(
    X=[
        ['red', 'car'],
        ['blue', 'car'],
        ['green', 'plane']
    ]
)
```

`
[[1, 0, 0], [0, 0, 0], [0, 1, 1]]
`

For a column:
```python
from categorical_encoder.encoder_service import EncoderService
encoder_service = EncoderService(encoder_type='binary')
print encoder_service.fit_transform_column(name="color", column=[
    'red', 'blue', 'green'
])
```

`
{'color_1': [0, 0, 1], 'color_0': [1, 0, 0]}
`

### Run demo/test
```
    $ make demo
    $ make test
```
