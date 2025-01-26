import tempfile
import sox
import torchaudio

class SoxMixNode:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"audio1": ("AUDIO",),
                             "audio2": ("AUDIO",)}}

    CATEGORY = "ComfyUI-SoX-Mixdown"

    RETURN_TYPES = ("AUDIO", )

    FUNCTION = "mixaudio"

    def mixaudio(self, audio1, audio2):
    # 一時ファイルの作成
        with tempfile.TemporaryDirectory() as str_temp_dir:
            print("temporary directory is:")
            print(str_temp_dir)
            file_path_1 = f"{str_temp_dir}/tempwaveform1.wav"
            file_path_2 = f"{str_temp_dir}/tempwaveform2.wav"
            file_path_3 = f"{str_temp_dir}/tempwaveform3.wav"

            with open(file_path_1, mode="w") as f1, \
                 open(file_path_2, mode="w") as f2, \
                 open(file_path_3, mode="w") as f3:

                # Soxを使って混合
                cbn = sox.Combiner()

                torchaudio.save(f1.name, audio1["waveform"][0],
                                audio1["sample_rate"], format="WAV")
                torchaudio.save(f2.name, audio2["waveform"][0],
                                audio2["sample_rate"], format="WAV")

                inputs = [f1.name, f2.name]
                cbn.build(inputs, f3.name, 'mix')

                waveform_3, sample_rate_3 = torchaudio.load(f3.name)

                return ({"waveform": waveform_3.unsqueeze(0),
                         "sample_rate": sample_rate_3}, )

NODE_CLASS_MAPPINGS = {
    "SoxMixNode": SoxMixNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SoxMixNode": "SoxMixNode",
}
