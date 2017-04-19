"""Test module for categorical_encoder
"""
from categorical_encoder.encoder_service import EncoderService


class TestEncodingService(object):
    """TestEncodingService class provides methods for testing EncoderService
    """

    def test_binary(self):
        """Test binary encoding
        """

        data = ["red", "green", "blue"]
        encoder_service = EncoderService(encoder_type='binary')
        encoder_service.fit_transform_column(name="color", column=data)

        assert sorted(encoder_service.encoders[
            "color"
        ].translation_dict.keys()) == sorted([
            "red", "green", "blue"
        ])
        assert len(
            encoder_service.encoders["color"].translation_dict['red']
        ) == 2

    def test_ordinal(self):
        """Test ordinal encoding
        """

        data = ["red", "green", "blue"]
        encoder_service = EncoderService(encoder_type='ordinal')
        encoder_service.fit_transform_column(name="color", column=data)

        assert sorted(encoder_service.encoders[
            "color"
        ].translation_dict.keys()) == sorted([
            "red", "green", "blue"
        ])
        assert encoder_service.encoders["color"].translation_dict['red'] < 3
        assert encoder_service.encoders["color"].translation_dict['red'] >= 0
