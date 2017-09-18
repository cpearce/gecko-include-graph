# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

media_cpp_files = [
  ("dom/media/","ADTSDecoder.cpp"),
  ("dom/media/","ADTSDemuxer.cpp"),
  # ("dom/media/","AudioCaptureStream.cpp"),
  # ("dom/media/","AudioChannelFormat.cpp"),
  # ("dom/media/","AudioCompactor.cpp"),
  ("dom/media/","AudioConverter.cpp"),
  # ("dom/media/","AudioDeviceInfo.cpp"),
  # ("dom/media/","AudioNotificationReceiver.cpp"),
  # ("dom/media/","AudioNotificationSender.cpp"),
  # ("dom/media/","AudioSegment.cpp"),
  ("dom/media/","AudioStream.cpp"),
  # ("dom/media/","AudioStreamTrack.cpp"),
  # ("dom/media/","AudioTrack.cpp"),
  # ("dom/media/","AudioTrackList.cpp"),
  # ("dom/media/","Benchmark.cpp"),
  # ("dom/media/bridge/","MediaModule.cpp"),
  # ("dom/media/","CanvasCaptureMediaStream.cpp"),
  ("dom/media/","ChannelMediaDecoder.cpp"),
  ("dom/media/","CubebUtils.cpp"),
  # ("dom/media/","DecoderDoctorDiagnostics.cpp"),
  ("dom/media/","DecoderTraits.cpp"),
  # ("dom/media/","DOMMediaStream.cpp"),
  # ("dom/media/eme/","CDMCaps.cpp"),
  # ("dom/media/eme/","DetailedPromise.cpp"),
  # ("dom/media/eme/","EMEUtils.cpp"),
  # ("dom/media/eme/mediadrm/","MediaDrmCDMCallbackProxy.cpp"),
  # ("dom/media/eme/mediadrm/","MediaDrmCDMProxy.cpp"),
  # ("dom/media/eme/mediadrm/","MediaDrmProxySupport.cpp"),
  # ("dom/media/eme/","MediaEncryptedEvent.cpp"),
  # ("dom/media/eme/","MediaKeyError.cpp"),
  # ("dom/media/eme/","MediaKeyMessageEvent.cpp"),
  # ("dom/media/eme/","MediaKeys.cpp"),
  # ("dom/media/eme/","MediaKeySession.cpp"),
  # ("dom/media/eme/","MediaKeyStatusMap.cpp"),
  # ("dom/media/eme/","MediaKeySystemAccess.cpp"),
  # ("dom/media/eme/","MediaKeySystemAccessManager.cpp"),
  # ("dom/media/","EncodedBufferCache.cpp"),
  # ("dom/media/encoder/","MediaEncoder.cpp"),
  # ("dom/media/encoder/","OpusTrackEncoder.cpp"),
  # ("dom/media/encoder/","TrackEncoder.cpp"),
  # ("dom/media/encoder/","VP8TrackEncoder.cpp"),
  # ("dom/media/","FileBlockCache.cpp"),
  ("dom/media/flac/","FlacDecoder.cpp"),
  ("dom/media/flac/","FlacDemuxer.cpp"),
  ("dom/media/flac/","FlacFrameParser.cpp"),
  ("dom/media/fmp4/","MP4Decoder.cpp"),
  ("dom/media/fmp4/","MP4Demuxer.cpp"),
  # ("dom/media/","GetUserMediaRequest.cpp"),
  # ("dom/media/gmp/","ChromiumCDMAdapter.cpp"),
  # ("dom/media/gmp/","ChromiumCDMChild.cpp"),
  # ("dom/media/gmp/","ChromiumCDMParent.cpp"),
  # ("dom/media/gmp/","ChromiumCDMProxy.cpp"),
  # ("dom/media/gmp/","DecryptJob.cpp"),
  # ("dom/media/gmp/","GMPCDMCallbackProxy.cpp"),
  # ("dom/media/gmp/","GMPCDMProxy.cpp"),
  # ("dom/media/gmp/","GMPChild.cpp"),
  # ("dom/media/gmp/","GMPContentChild.cpp"),
  # ("dom/media/gmp/","GMPContentParent.cpp"),
  # ("dom/media/gmp/","GMPCrashHelper.cpp"),
  # ("dom/media/gmp/","GMPCrashHelperHolder.cpp"),
  # ("dom/media/gmp/","GMPDecryptorChild.cpp"),
  # ("dom/media/gmp/","GMPDecryptorParent.cpp"),
  # ("dom/media/gmp/","GMPDiskStorage.cpp"),
  # ("dom/media/gmp/","GMPEncryptedBufferDataImpl.cpp"),
  # ("dom/media/gmp/","GMPLoader.cpp"),
  # ("dom/media/gmp/","GMPMemoryStorage.cpp"),
  # ("dom/media/gmp/","GMPParent.cpp"),
  # ("dom/media/gmp/","GMPPlatform.cpp"),
  # ("dom/media/gmp/","GMPProcessChild.cpp"),
  # ("dom/media/gmp/","GMPProcessParent.cpp"),
  # ("dom/media/gmp/","GMPService.cpp"),
  # ("dom/media/gmp/","GMPServiceChild.cpp"),
  # ("dom/media/gmp/","GMPServiceParent.cpp"),
  # ("dom/media/gmp/","GMPSharedMemManager.cpp"),
  # ("dom/media/gmp/","GMPStorageChild.cpp"),
  # ("dom/media/gmp/","GMPStorageParent.cpp"),
  # ("dom/media/gmp/","GMPTimerChild.cpp"),
  # ("dom/media/gmp/","GMPTimerParent.cpp"),
  # ("dom/media/gmp/","GMPUtils.cpp"),
  # ("dom/media/gmp/","GMPVideoDecoderChild.cpp"),
  # ("dom/media/gmp/","GMPVideoDecoderParent.cpp"),
  # ("dom/media/gmp/","GMPVideoEncodedFrameImpl.cpp"),
  # ("dom/media/gmp/","GMPVideoEncoderChild.cpp"),
  # ("dom/media/gmp/","GMPVideoEncoderParent.cpp"),
  # ("dom/media/gmp/","GMPVideoHost.cpp"),
  # ("dom/media/gmp/","GMPVideoi420FrameImpl.cpp"),
  # ("dom/media/gmp/","GMPVideoPlaneImpl.cpp"),
  # ("dom/media/gmp/widevine-adapter/","WidevineAdapter.cpp"),
  # ("dom/media/gmp/widevine-adapter/","WidevineDecryptor.cpp"),
  # ("dom/media/gmp/widevine-adapter/","WidevineDummyDecoder.cpp"),
  # ("dom/media/gmp/widevine-adapter/","WidevineFileIO.cpp"),
  # ("dom/media/gmp/widevine-adapter/","WidevineUtils.cpp"),
  # ("dom/media/gmp/widevine-adapter/","WidevineVideoDecoder.cpp"),
  # ("dom/media/gmp/widevine-adapter/","WidevineVideoFrame.cpp"),
  # ("dom/media/gmp-plugin/gmp-","fake.cpp"),
  # ("dom/media/gmp-plugin/gmp-test-","decryptor.cpp"),
  # ("dom/media/gmp-plugin/gmp-test-","storage.cpp"),
  # ("dom/media/gmp-plugin-openh264/gmp-fake-","openh264.cpp"),
  # ("dom/media/","GraphDriver.cpp"),
  # ("dom/media/gtest/","MockMediaResource.cpp"),
  # ("dom/media/gtest/","TestAudioBuffers.cpp"),
  # ("dom/media/gtest/","TestAudioCompactor.cpp"),
  # ("dom/media/gtest/","TestAudioMixer.cpp"),
  # ("dom/media/gtest/","TestAudioPacketizer.cpp"),
  # ("dom/media/gtest/","TestAudioSegment.cpp"),
  # ("dom/media/gtest/","TestBlankVideoDataCreator.cpp"),
  # ("dom/media/gtest/","TestGMPCrossOrigin.cpp"),
  # ("dom/media/gtest/","TestGMPRemoveAndDelete.cpp"),
  # ("dom/media/gtest/","TestGMPUtils.cpp"),
  # ("dom/media/gtest/","TestIntervalSet.cpp"),
  # ("dom/media/gtest/","TestMediaDataDecoder.cpp"),
  # ("dom/media/gtest/","TestMediaEventSource.cpp"),
  # ("dom/media/gtest/","TestMediaMIMETypes.cpp"),
  # ("dom/media/gtest/","TestMP3Demuxer.cpp"),
  # ("dom/media/gtest/","TestMP4Demuxer.cpp"),
  # ("dom/media/gtest/","TestRust.cpp"),
  # ("dom/media/gtest/","TestTimeUnit.cpp"),
  # ("dom/media/gtest/","TestTrackEncoder.cpp"),
  # ("dom/media/gtest/","TestVideoSegment.cpp"),
  # ("dom/media/gtest/","TestVideoTrackEncoder.cpp"),
  # ("dom/media/gtest/","TestVideoUtils.cpp"),
  # ("dom/media/gtest/","TestVPXDecoding.cpp"),
  # ("dom/media/gtest/","TestWebMBuffered.cpp"),
  # ("dom/media/gtest/","TestWebMWriter.cpp"),
  # ("dom/media/hls/","HLSDecoder.cpp"),
  # ("dom/media/hls/","HLSDemuxer.cpp"),
  # ("dom/media/hls/","HLSResource.cpp"),
  # ("dom/media/hls/","HLSUtils.cpp"),
  # ("dom/media/imagecapture/","CaptureTask.cpp"),
  # ("dom/media/imagecapture/","ImageCapture.cpp"),
  # ("dom/media/ipc/","RemoteVideoDecoder.cpp"),
  # ("dom/media/ipc/","VideoDecoderChild.cpp"),
  # ("dom/media/ipc/","VideoDecoderManagerChild.cpp"),
  # ("dom/media/ipc/","VideoDecoderManagerParent.cpp"),
  # ("dom/media/ipc/","VideoDecoderParent.cpp"),
  # ("dom/media/","Latency.cpp"),
  # ("dom/media/","MediaCache.cpp"),
  ("dom/media/","MediaContainerType.cpp"),
  ("dom/media/","MediaData.cpp"),
  ("dom/media/","MediaDecoder.cpp"),
  ("dom/media/","MediaDecoderStateMachine.cpp"),
  # ("dom/media/","MediaDeviceInfo.cpp"),
  # ("dom/media/","MediaDevices.cpp"),
  ("dom/media/","MediaFormatReader.cpp"),
  ("dom/media/","MediaInfo.cpp"),
  # ("dom/media/","MediaManager.cpp"),
  ("dom/media/","MediaMIMETypes.cpp"),
  ("dom/media/","MediaPrefs.cpp"),
  # ("dom/media/","MediaRecorder.cpp"),
  # ("dom/media/","MediaResource.cpp"),
  ("dom/media/","MediaShutdownManager.cpp"),
  ("dom/media/mediasink/","AudioSink.cpp"),
  ("dom/media/mediasink/","AudioSinkWrapper.cpp"),
  # ("dom/media/mediasink/","DecodedStream.cpp"),
  # ("dom/media/mediasink/","OutputStreamManager.cpp"),
  ("dom/media/mediasink/","VideoSink.cpp"),
  ("dom/media/mediasource/","ContainerParser.cpp"),
  # ("dom/media/mediasource/gtest/","TestContainerParser.cpp"),
  ("dom/media/mediasource/","MediaSource.cpp"),
  ("dom/media/mediasource/","MediaSourceDecoder.cpp"),
  ("dom/media/mediasource/","MediaSourceDemuxer.cpp"),
  ("dom/media/mediasource/","MediaSourceUtils.cpp"),
  ("dom/media/mediasource/","ResourceQueue.cpp"),
  ("dom/media/mediasource/","SourceBuffer.cpp"),
  ("dom/media/mediasource/","SourceBufferList.cpp"),
  ("dom/media/mediasource/","SourceBufferResource.cpp"),
  ("dom/media/mediasource/","TrackBuffersManager.cpp"),
  # ("dom/media/","MediaStreamError.cpp"),
  # ("dom/media/","MediaStreamGraph.cpp"),
  # ("dom/media/","MediaStreamListener.cpp"),
  # ("dom/media/","MediaStreamTrack.cpp"),
  # ("dom/media/","MediaStreamVideoSink.cpp"),
  ("dom/media/","MediaTimer.cpp"),
  # ("dom/media/","MediaTrack.cpp"),
  # ("dom/media/","MediaTrackList.cpp"),
  # ("dom/media/","MemoryBlockCache.cpp"),
  ("dom/media/mp3/","MP3Decoder.cpp"),
  ("dom/media/mp3/","MP3Demuxer.cpp"),
  ("dom/media/mp3/","MP3FrameParser.cpp"),
  ("dom/media/ogg/","OggCodecState.cpp"),
  ("dom/media/ogg/","OggCodecStore.cpp"),
  ("dom/media/ogg/","OggDecoder.cpp"),
  ("dom/media/ogg/","OggDemuxer.cpp"),
  # ("dom/media/ogg/","OggWriter.cpp"),
  ("dom/media/ogg/","OpusParser.cpp"),
  ("dom/media/platforms/agnostic/","AgnosticDecoderModule.cpp"),
  ("dom/media/platforms/agnostic/","AOMDecoder.cpp"),
  ("dom/media/platforms/agnostic/","BlankDecoderModule.cpp"),
  ("dom/media/platforms/agnostic/","DummyMediaDataDecoder.cpp"),
  # ("dom/media/platforms/agnostic/eme/","ChromiumCDMVideoDecoder.cpp"),
  # ("dom/media/platforms/agnostic/eme/","EMEDecoderModule.cpp"),
  # ("dom/media/platforms/agnostic/eme/","EMEVideoDecoder.cpp"),
  # ("dom/media/platforms/agnostic/eme/","SamplesWaitingForKey.cpp"),
  # ("dom/media/platforms/agnostic/gmp/","GMPDecoderModule.cpp"),
  # ("dom/media/platforms/agnostic/gmp/","GMPVideoDecoder.cpp"),
  ("dom/media/platforms/agnostic/","NullDecoderModule.cpp"),
  ("dom/media/platforms/agnostic/","OpusDecoder.cpp"),
  ("dom/media/platforms/agnostic/","TheoraDecoder.cpp"),
  ("dom/media/platforms/agnostic/","VorbisDecoder.cpp"),
  ("dom/media/platforms/agnostic/","VPXDecoder.cpp"),
  ("dom/media/platforms/agnostic/","WAVDecoder.cpp"),
  ("dom/media/platforms/android/","AndroidDecoderModule.cpp"),
  ("dom/media/platforms/android/","RemoteDataDecoder.cpp"),
  ("dom/media/platforms/apple/","AppleATDecoder.cpp"),
  ("dom/media/platforms/apple/","AppleCMLinker.cpp"),
  ("dom/media/platforms/apple/","AppleDecoderModule.cpp"),
  ("dom/media/platforms/apple/","AppleVTDecoder.cpp"),
  ("dom/media/platforms/apple/","AppleVTLinker.cpp"),
  ("dom/media/platforms/ffmpeg/","FFmpegAudioDecoder.cpp"),
  ("dom/media/platforms/ffmpeg/","FFmpegDataDecoder.cpp"),
  ("dom/media/platforms/ffmpeg/","FFmpegDecoderModule.cpp"),
  ("dom/media/platforms/ffmpeg/","FFmpegLibWrapper.cpp"),
  ("dom/media/platforms/ffmpeg/","FFmpegRuntimeLinker.cpp"),
  ("dom/media/platforms/ffmpeg/","FFmpegVideoDecoder.cpp"),
  ("dom/media/platforms/ffmpeg/ffvpx/","FFVPXRuntimeLinker.cpp"),
  ("dom/media/platforms/omx/","OmxDataDecoder.cpp"),
  ("dom/media/platforms/omx/","OmxDecoderModule.cpp"),
  ("dom/media/platforms/omx/","OmxPlatformLayer.cpp"),
  ("dom/media/platforms/omx/","OmxPromiseLayer.cpp"),
  ("dom/media/platforms/","PDMFactory.cpp"),
  ("dom/media/platforms/wmf/","DXVA2Manager.cpp"),
  ("dom/media/platforms/wmf/","MFTDecoder.cpp"),
  ("dom/media/platforms/wmf/","WMFAudioMFTManager.cpp"),
  ("dom/media/platforms/wmf/","WMFDecoderModule.cpp"),
  ("dom/media/platforms/wmf/","WMFMediaDataDecoder.cpp"),
  ("dom/media/platforms/wmf/","WMFUtils.cpp"),
  ("dom/media/platforms/wmf/","WMFVideoMFTManager.cpp"),
  ("dom/media/platforms/wrappers/","H264Converter.cpp"),
  ("dom/media/platforms/wrappers/","MediaDataDecoderProxy.cpp"),
  # ("dom/media/","QueueObject.cpp"),
  ("dom/media/","ReaderProxy.cpp"),
  ("dom/media/","SeekJob.cpp"),
  # ("dom/media/","StreamTracks.cpp"),
  # ("dom/media/systemservices/","CamerasChild.cpp"),
  # ("dom/media/systemservices/","CamerasParent.cpp"),
  # ("dom/media/systemservices/","MediaChild.cpp"),
  # ("dom/media/systemservices/","MediaParent.cpp"),
  # ("dom/media/systemservices/","MediaSystemResourceClient.cpp"),
  # ("dom/media/systemservices/","MediaSystemResourceManager.cpp"),
  # ("dom/media/systemservices/","MediaSystemResourceManagerChild.cpp"),
  # ("dom/media/systemservices/","MediaSystemResourceManagerParent.cpp"),
  # ("dom/media/systemservices/","MediaSystemResourceService.cpp"),
  # ("dom/media/systemservices/","MediaUtils.cpp"),
  # ("dom/media/systemservices/","OpenSLESProvider.cpp"),
  # ("dom/media/systemservices/","OSXRunLoopSingleton.cpp"),
  # ("dom/media/systemservices/","ShmemPool.cpp"),
  # ("dom/media/systemservices/","VideoEngine.cpp"),
  # ("dom/media/systemservices/","VideoFrameUtils.cpp"),
  # ("dom/media/","TextTrack.cpp"),
  # ("dom/media/","TextTrackCue.cpp"),
  # ("dom/media/","TextTrackCueList.cpp"),
  # ("dom/media/","TextTrackList.cpp"),
  # ("dom/media/","TextTrackRegion.cpp"),
  ("dom/media/","ThreadPoolCOMListener.cpp"),
  # ("dom/media/","TrackUnionStream.cpp"),
  # ("dom/media/","VideoFrameContainer.cpp"),
  # ("dom/media/","VideoPlaybackQuality.cpp"),
  # ("dom/media/","VideoSegment.cpp"),
  # ("dom/media/","VideoStreamTrack.cpp"),
  # ("dom/media/","VideoTrack.cpp"),
  # ("dom/media/","VideoTrackList.cpp"),
  ("dom/media/","VideoUtils.cpp"),
  ("dom/media/wave/","WaveDecoder.cpp"),
  ("dom/media/wave/","WaveDemuxer.cpp"),
  # ("dom/media/webaudio/","AnalyserNode.cpp"),
  # ("dom/media/webaudio/","AudioBlock.cpp"),
  # ("dom/media/webaudio/","AudioBuffer.cpp"),
  # ("dom/media/webaudio/","AudioBufferSourceNode.cpp"),
  # ("dom/media/webaudio/","AudioContext.cpp"),
  # ("dom/media/webaudio/","AudioDestinationNode.cpp"),
  # ("dom/media/webaudio/","AudioEventTimeline.cpp"),
  # ("dom/media/webaudio/","AudioListener.cpp"),
  # ("dom/media/webaudio/","AudioNode.cpp"),
  # ("dom/media/webaudio/","AudioNodeEngine.cpp"),
  # ("dom/media/webaudio/","AudioNodeEngineNEON.cpp"),
  # ("dom/media/webaudio/","AudioNodeEngineSSE2.cpp"),
  # ("dom/media/webaudio/","AudioNodeExternalInputStream.cpp"),
  # ("dom/media/webaudio/","AudioNodeStream.cpp"),
  # ("dom/media/webaudio/","AudioParam.cpp"),
  # ("dom/media/webaudio/","AudioProcessingEvent.cpp"),
  # ("dom/media/webaudio/","AudioScheduledSourceNode.cpp"),
  # ("dom/media/webaudio/","BiquadFilterNode.cpp"),
  # ("dom/media/webaudio/blink/","Biquad.cpp"),
  # ("dom/media/webaudio/blink/","DynamicsCompressor.cpp"),
  # ("dom/media/webaudio/blink/","DynamicsCompressorKernel.cpp"),
  # ("dom/media/webaudio/blink/","FFTConvolver.cpp"),
  # ("dom/media/webaudio/blink/","HRTFDatabase.cpp"),
  # ("dom/media/webaudio/blink/","HRTFDatabaseLoader.cpp"),
  # ("dom/media/webaudio/blink/","HRTFElevation.cpp"),
  # ("dom/media/webaudio/blink/","HRTFKernel.cpp"),
  # ("dom/media/webaudio/blink/","HRTFPanner.cpp"),
  # ("dom/media/webaudio/blink/","IIRFilter.cpp"),
  # ("dom/media/webaudio/blink/IRC_Composite_C_R0195-","incl.cpp"),
  # ("dom/media/webaudio/blink/","PeriodicWave.cpp"),
  # ("dom/media/webaudio/blink/","Reverb.cpp"),
  # ("dom/media/webaudio/blink/","ReverbAccumulationBuffer.cpp"),
  # ("dom/media/webaudio/blink/","ReverbConvolver.cpp"),
  # ("dom/media/webaudio/blink/","ReverbConvolverStage.cpp"),
  # ("dom/media/webaudio/blink/","ReverbInputBuffer.cpp"),
  # ("dom/media/webaudio/blink/","ZeroPole.cpp"),
  # ("dom/media/webaudio/","ChannelMergerNode.cpp"),
  # ("dom/media/webaudio/","ChannelSplitterNode.cpp"),
  # ("dom/media/webaudio/","ConstantSourceNode.cpp"),
  # ("dom/media/webaudio/","ConvolverNode.cpp"),
  # ("dom/media/webaudio/","DelayBuffer.cpp"),
  # ("dom/media/webaudio/","DelayNode.cpp"),
  # ("dom/media/webaudio/","DynamicsCompressorNode.cpp"),
  # ("dom/media/webaudio/","FFTBlock.cpp"),
  # ("dom/media/webaudio/","GainNode.cpp"),
  # ("dom/media/webaudio/gtest/","TestAudioEventTimeline.cpp"),
  # ("dom/media/webaudio/","IIRFilterNode.cpp"),
  # ("dom/media/webaudio/","MediaBufferDecoder.cpp"),
  # ("dom/media/webaudio/","MediaElementAudioSourceNode.cpp"),
  # ("dom/media/webaudio/","MediaStreamAudioDestinationNode.cpp"),
  # ("dom/media/webaudio/","MediaStreamAudioSourceNode.cpp"),
  # ("dom/media/webaudio/","OscillatorNode.cpp"),
  # ("dom/media/webaudio/","PannerNode.cpp"),
  # ("dom/media/webaudio/","PeriodicWave.cpp"),
  # ("dom/media/webaudio/","ScriptProcessorNode.cpp"),
  # ("dom/media/webaudio/","StereoPannerNode.cpp"),
  # ("dom/media/webaudio/","ThreeDPoint.cpp"),
  # ("dom/media/webaudio/","WaveShaperNode.cpp"),
  # ("dom/media/webaudio/","WebAudioUtils.cpp"),
  # ("dom/media/webm/","EbmlComposer.cpp"),
  ("dom/media/webm/","WebMBufferedParser.cpp"),
  ("dom/media/webm/","WebMDecoder.cpp"),
  ("dom/media/webm/","WebMDemuxer.cpp"),
  # ("dom/media/webm/","WebMWriter.cpp"),
  # ("dom/media/webrtc/","MediaEngineCameraVideoSource.cpp"),
  # ("dom/media/webrtc/","MediaEngineDefault.cpp"),
  # ("dom/media/webrtc/","MediaEngineRemoteVideoSource.cpp"),
  # ("dom/media/webrtc/","MediaEngineTabVideoSource.cpp"),
  # ("dom/media/webrtc/","MediaEngineWebRTC.cpp"),
  # ("dom/media/webrtc/","MediaEngineWebRTCAudio.cpp"),
  # ("dom/media/webrtc/","MediaTrackConstraints.cpp"),
  # ("dom/media/webrtc/","PeerIdentity.cpp"),
  # ("dom/media/webrtc/","RTCCertificate.cpp"),
  # ("dom/media/webrtc/","RTCIdentityProviderRegistrar.cpp"),
  # ("dom/media/webspeech/recognition/","PocketSphinxSpeechRecognitionService.cpp"),
  # ("dom/media/webspeech/recognition/","SpeechGrammar.cpp"),
  # ("dom/media/webspeech/recognition/","SpeechGrammarList.cpp"),
  # ("dom/media/webspeech/recognition/","SpeechRecognition.cpp"),
  # ("dom/media/webspeech/recognition/","SpeechRecognitionAlternative.cpp"),
  # ("dom/media/webspeech/recognition/","SpeechRecognitionResult.cpp"),
  # ("dom/media/webspeech/recognition/","SpeechRecognitionResultList.cpp"),
  # ("dom/media/webspeech/recognition/","SpeechStreamListener.cpp"),
  # ("dom/media/webspeech/recognition/test/","FakeSpeechRecognitionService.cpp"),
  # ("dom/media/webspeech/synth/cocoa/","OSXSpeechSynthesizerModule.cpp"),
  # ("dom/media/webspeech/synth/ipc/","SpeechSynthesisChild.cpp"),
  # ("dom/media/webspeech/synth/ipc/","SpeechSynthesisParent.cpp"),
  # ("dom/media/webspeech/synth/","nsSpeechTask.cpp"),
  # ("dom/media/webspeech/synth/","nsSynthVoiceRegistry.cpp"),
  # ("dom/media/webspeech/synth/pico/","nsPicoService.cpp"),
  # ("dom/media/webspeech/synth/pico/","PicoModule.cpp"),
  # ("dom/media/webspeech/synth/speechd/","SpeechDispatcherModule.cpp"),
  # ("dom/media/webspeech/synth/speechd/","SpeechDispatcherService.cpp"),
  # ("dom/media/webspeech/synth/","SpeechSynthesis.cpp"),
  # ("dom/media/webspeech/synth/","SpeechSynthesisUtterance.cpp"),
  # ("dom/media/webspeech/synth/","SpeechSynthesisVoice.cpp"),
  # ("dom/media/webspeech/synth/test/","FakeSynthModule.cpp"),
  # ("dom/media/webspeech/synth/test/","nsFakeSynthServices.cpp"),
  # ("dom/media/webspeech/synth/windows/","SapiModule.cpp"),
  # ("dom/media/webspeech/synth/windows/","SapiService.cpp"),
  # ("dom/media/","WebVTTListener.cpp"),
  ("dom/media/","XiphExtradata.cpp"),
]