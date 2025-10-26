#! /bin/bash
STATUS_REPORT="$1"
tts --text "$STATUS_REPORT" --use_cuda True \
    --model_name "tts_models/en/ljspeech/glow-tts" \
    --pipe_out | aplay