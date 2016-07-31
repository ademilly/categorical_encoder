## (Mostly Binary) encoder

Inspired by http://www.willmcginnis.com/2015/11/29/beyond-one-hot-an-exploration-of-categorical-variables/

###Setup categorical_encoder package

`
    $ python setup.py install
`

###Usage
```
import categorical_encoder
encoder_service = categorical_encoder.EncoderService(encoder_type='binary')
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

###Setup demo

`
    $ ./setup.sh
`

###Run demo

`
    $ ./run_demo.sh
`
