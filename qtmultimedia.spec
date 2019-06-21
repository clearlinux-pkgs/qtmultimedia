#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : qtmultimedia
Version  : 5.12.4
Release  : 18
URL      : https://download.qt.io/official_releases/qt/5.12/5.12.4/submodules/qtmultimedia-everywhere-src-5.12.4.tar.xz
Source0  : https://download.qt.io/official_releases/qt/5.12/5.12.4/submodules/qtmultimedia-everywhere-src-5.12.4.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.3 GPL-2.0 GPL-3.0 LGPL-2.1 LGPL-3.0
Requires: qtmultimedia-lib = %{version}-%{release}
Requires: qtmultimedia-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-qmake
BuildRequires : mesa-dev
BuildRequires : pkgconfig(Qt5Core)
BuildRequires : pkgconfig(Qt5Gui)
BuildRequires : pkgconfig(Qt5Network)
BuildRequires : pkgconfig(Qt5OpenGL)
BuildRequires : pkgconfig(Qt5Qml)
BuildRequires : pkgconfig(Qt5Quick)
BuildRequires : pkgconfig(Qt5Test)
BuildRequires : pkgconfig(Qt5Widgets)
BuildRequires : pkgconfig(gstreamer-1.0)
BuildRequires : pkgconfig(gstreamer-app-1.0)
BuildRequires : pkgconfig(gstreamer-audio-1.0)
BuildRequires : pkgconfig(gstreamer-base-1.0)
BuildRequires : pkgconfig(gstreamer-pbutils-1.0)
BuildRequires : pkgconfig(gstreamer-video-1.0)
BuildRequires : pkgconfig(libpulse)
BuildRequires : pkgconfig(libpulse-mainloop-glib)
BuildRequires : pkgconfig(openal)

%description
This example performs some simple OpenCL operations on camera or video input
which is assumed to be provided in RGB format. The OpenCL operation is done on
an OpenGL texture using CL-GL interop, without any further readbacks or copies
(except for the initial texture upload, when necessary).

%package dev
Summary: dev components for the qtmultimedia package.
Group: Development
Requires: qtmultimedia-lib = %{version}-%{release}
Provides: qtmultimedia-devel = %{version}-%{release}
Requires: qtmultimedia = %{version}-%{release}

%description dev
dev components for the qtmultimedia package.


%package lib
Summary: lib components for the qtmultimedia package.
Group: Libraries
Requires: qtmultimedia-license = %{version}-%{release}

%description lib
lib components for the qtmultimedia package.


%package license
Summary: license components for the qtmultimedia package.
Group: Default

%description license
license components for the qtmultimedia package.


%prep
%setup -q -n qtmultimedia-everywhere-src-5.12.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export GCC_IGNORE_WERROR=1
%qmake QMAKE_CFLAGS+=-fno-lto QMAKE_CXXFLAGS+=-fno-lto
test -r config.log && cat config.log
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1561150156
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qtmultimedia
cp LICENSE.FDL %{buildroot}/usr/share/package-licenses/qtmultimedia/LICENSE.FDL
cp LICENSE.GPL2 %{buildroot}/usr/share/package-licenses/qtmultimedia/LICENSE.GPL2
cp LICENSE.GPL3 %{buildroot}/usr/share/package-licenses/qtmultimedia/LICENSE.GPL3
cp LICENSE.GPL3-EXCEPT %{buildroot}/usr/share/package-licenses/qtmultimedia/LICENSE.GPL3-EXCEPT
cp LICENSE.LGPL3 %{buildroot}/usr/share/package-licenses/qtmultimedia/LICENSE.LGPL3
cp examples/multimedia/spectrum/3rdparty/fftreal/license.txt %{buildroot}/usr/share/package-licenses/qtmultimedia/examples_multimedia_spectrum_3rdparty_fftreal_license.txt
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/qt5/QtMultimedia/5.12.4/QtMultimedia/private/gstvideoconnector_p.h
/usr/include/qt5/QtMultimedia/5.12.4/QtMultimedia/private/qabstractvideobuffer_p.h
/usr/include/qt5/QtMultimedia/5.12.4/QtMultimedia/private/qaudiobuffer_p.h
/usr/include/qt5/QtMultimedia/5.12.4/QtMultimedia/private/qaudiodevicefactory_p.h
/usr/include/qt5/QtMultimedia/5.12.4/QtMultimedia/private/qaudiohelpers_p.h
/usr/include/qt5/QtMultimedia/5.12.4/QtMultimedia/private/qaudiosystempluginext_p.h
/usr/include/qt5/QtMultimedia/5.12.4/QtMultimedia/private/qcamera_p.h
/usr/include/qt5/QtMultimedia/5.12.4/QtMultimedia/private/qdeclarativevideooutput_backend_p.h
/usr/include/qt5/QtMultimedia/5.12.4/QtMultimedia/private/qdeclarativevideooutput_p.h
/usr/include/qt5/QtMultimedia/5.12.4/QtMultimedia/private/qgstappsrc_p.h
/usr/include/qt5/QtMultimedia/5.12.4/QtMultimedia/private/qgstbufferpoolinterface_p.h
/usr/include/qt5/QtMultimedia/5.12.4/QtMultimedia/private/qgstcodecsinfo_p.h
/usr/include/qt5/QtMultimedia/5.12.4/QtMultimedia/private/qgstreameraudioinputselector_p.h
/usr/include/qt5/QtMultimedia/5.12.4/QtMultimedia/private/qgstreameraudioprobecontrol_p.h
/usr/include/qt5/QtMultimedia/5.12.4/QtMultimedia/private/qgstreamerbufferprobe_p.h
/usr/include/qt5/QtMultimedia/5.12.4/QtMultimedia/private/qgstreamerbushelper_p.h
/usr/include/qt5/QtMultimedia/5.12.4/QtMultimedia/private/qgstreamermessage_p.h
/usr/include/qt5/QtMultimedia/5.12.4/QtMultimedia/private/qgstreamermirtexturerenderer_p.h
/usr/include/qt5/QtMultimedia/5.12.4/QtMultimedia/private/qgstreamerplayercontrol_p.h
/usr/include/qt5/QtMultimedia/5.12.4/QtMultimedia/private/qgstreamerplayersession_p.h
/usr/include/qt5/QtMultimedia/5.12.4/QtMultimedia/private/qgstreamervideoinputdevicecontrol_p.h
/usr/include/qt5/QtMultimedia/5.12.4/QtMultimedia/private/qgstreamervideooverlay_p.h
/usr/include/qt5/QtMultimedia/5.12.4/QtMultimedia/private/qgstreamervideoprobecontrol_p.h
/usr/include/qt5/QtMultimedia/5.12.4/QtMultimedia/private/qgstreamervideorenderer_p.h
/usr/include/qt5/QtMultimedia/5.12.4/QtMultimedia/private/qgstreamervideorendererinterface_p.h
/usr/include/qt5/QtMultimedia/5.12.4/QtMultimedia/private/qgstreamervideowidget_p.h
/usr/include/qt5/QtMultimedia/5.12.4/QtMultimedia/private/qgstreamervideowindow_p.h
/usr/include/qt5/QtMultimedia/5.12.4/QtMultimedia/private/qgsttools_global_p.h
/usr/include/qt5/QtMultimedia/5.12.4/QtMultimedia/private/qgstutils_p.h
/usr/include/qt5/QtMultimedia/5.12.4/QtMultimedia/private/qgstvideobuffer_p.h
/usr/include/qt5/QtMultimedia/5.12.4/QtMultimedia/private/qgstvideorendererplugin_p.h
/usr/include/qt5/QtMultimedia/5.12.4/QtMultimedia/private/qgstvideorenderersink_p.h
/usr/include/qt5/QtMultimedia/5.12.4/QtMultimedia/private/qimagevideobuffer_p.h
/usr/include/qt5/QtMultimedia/5.12.4/QtMultimedia/private/qmediacontrol_p.h
/usr/include/qt5/QtMultimedia/5.12.4/QtMultimedia/private/qmedianetworkplaylistprovider_p.h
/usr/include/qt5/QtMultimedia/5.12.4/QtMultimedia/private/qmediaobject_p.h
/usr/include/qt5/QtMultimedia/5.12.4/QtMultimedia/private/qmediaopenglhelper_p.h
/usr/include/qt5/QtMultimedia/5.12.4/QtMultimedia/private/qmediaplaylist_p.h
/usr/include/qt5/QtMultimedia/5.12.4/QtMultimedia/private/qmediaplaylistcontrol_p.h
/usr/include/qt5/QtMultimedia/5.12.4/QtMultimedia/private/qmediaplaylistioplugin_p.h
/usr/include/qt5/QtMultimedia/5.12.4/QtMultimedia/private/qmediaplaylistnavigator_p.h
/usr/include/qt5/QtMultimedia/5.12.4/QtMultimedia/private/qmediaplaylistprovider_p.h
/usr/include/qt5/QtMultimedia/5.12.4/QtMultimedia/private/qmediaplaylistsourcecontrol_p.h
/usr/include/qt5/QtMultimedia/5.12.4/QtMultimedia/private/qmediapluginloader_p.h
/usr/include/qt5/QtMultimedia/5.12.4/QtMultimedia/private/qmediarecorder_p.h
/usr/include/qt5/QtMultimedia/5.12.4/QtMultimedia/private/qmediaresourcepolicy_p.h
/usr/include/qt5/QtMultimedia/5.12.4/QtMultimedia/private/qmediaresourcepolicyplugin_p.h
/usr/include/qt5/QtMultimedia/5.12.4/QtMultimedia/private/qmediaresourceset_p.h
/usr/include/qt5/QtMultimedia/5.12.4/QtMultimedia/private/qmediaservice_p.h
/usr/include/qt5/QtMultimedia/5.12.4/QtMultimedia/private/qmediaserviceprovider_p.h
/usr/include/qt5/QtMultimedia/5.12.4/QtMultimedia/private/qmediastoragelocation_p.h
/usr/include/qt5/QtMultimedia/5.12.4/QtMultimedia/private/qmemoryvideobuffer_p.h
/usr/include/qt5/QtMultimedia/5.12.4/QtMultimedia/private/qmultimediautils_p.h
/usr/include/qt5/QtMultimedia/5.12.4/QtMultimedia/private/qplaylistfileparser_p.h
/usr/include/qt5/QtMultimedia/5.12.4/QtMultimedia/private/qsamplecache_p.h
/usr/include/qt5/QtMultimedia/5.12.4/QtMultimedia/private/qsgvideonode_p.h
/usr/include/qt5/QtMultimedia/5.12.4/QtMultimedia/private/qsoundeffect_pulse_p.h
/usr/include/qt5/QtMultimedia/5.12.4/QtMultimedia/private/qsoundeffect_qaudio_p.h
/usr/include/qt5/QtMultimedia/5.12.4/QtMultimedia/private/qtmultimedia-config_p.h
/usr/include/qt5/QtMultimedia/5.12.4/QtMultimedia/private/qtmultimediaglobal_p.h
/usr/include/qt5/QtMultimedia/5.12.4/QtMultimedia/private/qtmultimediaquickdefs_p.h
/usr/include/qt5/QtMultimedia/5.12.4/QtMultimedia/private/qvideoframe_p.h
/usr/include/qt5/QtMultimedia/5.12.4/QtMultimedia/private/qvideoframeconversionhelper_p.h
/usr/include/qt5/QtMultimedia/5.12.4/QtMultimedia/private/qvideooutputorientationhandler_p.h
/usr/include/qt5/QtMultimedia/5.12.4/QtMultimedia/private/qvideosurfacegstsink_p.h
/usr/include/qt5/QtMultimedia/5.12.4/QtMultimedia/private/qvideosurfaceoutput_p.h
/usr/include/qt5/QtMultimedia/5.12.4/QtMultimedia/private/qwavedecoder_p.h
/usr/include/qt5/QtMultimedia/QAbstractAudioDeviceInfo
/usr/include/qt5/QtMultimedia/QAbstractAudioInput
/usr/include/qt5/QtMultimedia/QAbstractAudioOutput
/usr/include/qt5/QtMultimedia/QAbstractPlanarVideoBuffer
/usr/include/qt5/QtMultimedia/QAbstractVideoBuffer
/usr/include/qt5/QtMultimedia/QAbstractVideoFilter
/usr/include/qt5/QtMultimedia/QAbstractVideoSurface
/usr/include/qt5/QtMultimedia/QAudio
/usr/include/qt5/QtMultimedia/QAudioBuffer
/usr/include/qt5/QtMultimedia/QAudioDecoder
/usr/include/qt5/QtMultimedia/QAudioDecoderControl
/usr/include/qt5/QtMultimedia/QAudioDeviceInfo
/usr/include/qt5/QtMultimedia/QAudioEncoderSettings
/usr/include/qt5/QtMultimedia/QAudioEncoderSettingsControl
/usr/include/qt5/QtMultimedia/QAudioFormat
/usr/include/qt5/QtMultimedia/QAudioInput
/usr/include/qt5/QtMultimedia/QAudioInputSelectorControl
/usr/include/qt5/QtMultimedia/QAudioOutput
/usr/include/qt5/QtMultimedia/QAudioOutputSelectorControl
/usr/include/qt5/QtMultimedia/QAudioProbe
/usr/include/qt5/QtMultimedia/QAudioRecorder
/usr/include/qt5/QtMultimedia/QAudioRoleControl
/usr/include/qt5/QtMultimedia/QAudioSystemFactoryInterface
/usr/include/qt5/QtMultimedia/QAudioSystemPlugin
/usr/include/qt5/QtMultimedia/QCamera
/usr/include/qt5/QtMultimedia/QCameraCaptureBufferFormatControl
/usr/include/qt5/QtMultimedia/QCameraCaptureDestinationControl
/usr/include/qt5/QtMultimedia/QCameraControl
/usr/include/qt5/QtMultimedia/QCameraExposure
/usr/include/qt5/QtMultimedia/QCameraExposureControl
/usr/include/qt5/QtMultimedia/QCameraFeedbackControl
/usr/include/qt5/QtMultimedia/QCameraFlashControl
/usr/include/qt5/QtMultimedia/QCameraFocus
/usr/include/qt5/QtMultimedia/QCameraFocusControl
/usr/include/qt5/QtMultimedia/QCameraFocusZone
/usr/include/qt5/QtMultimedia/QCameraFocusZoneList
/usr/include/qt5/QtMultimedia/QCameraImageCapture
/usr/include/qt5/QtMultimedia/QCameraImageCaptureControl
/usr/include/qt5/QtMultimedia/QCameraImageProcessing
/usr/include/qt5/QtMultimedia/QCameraImageProcessingControl
/usr/include/qt5/QtMultimedia/QCameraInfo
/usr/include/qt5/QtMultimedia/QCameraInfoControl
/usr/include/qt5/QtMultimedia/QCameraLocksControl
/usr/include/qt5/QtMultimedia/QCameraViewfinderSettings
/usr/include/qt5/QtMultimedia/QCameraViewfinderSettingsControl
/usr/include/qt5/QtMultimedia/QCameraViewfinderSettingsControl2
/usr/include/qt5/QtMultimedia/QCameraZoomControl
/usr/include/qt5/QtMultimedia/QCustomAudioRoleControl
/usr/include/qt5/QtMultimedia/QImageEncoderControl
/usr/include/qt5/QtMultimedia/QImageEncoderSettings
/usr/include/qt5/QtMultimedia/QMediaAudioProbeControl
/usr/include/qt5/QtMultimedia/QMediaAvailabilityControl
/usr/include/qt5/QtMultimedia/QMediaBindableInterface
/usr/include/qt5/QtMultimedia/QMediaContainerControl
/usr/include/qt5/QtMultimedia/QMediaContent
/usr/include/qt5/QtMultimedia/QMediaControl
/usr/include/qt5/QtMultimedia/QMediaGaplessPlaybackControl
/usr/include/qt5/QtMultimedia/QMediaMetaData
/usr/include/qt5/QtMultimedia/QMediaNetworkAccessControl
/usr/include/qt5/QtMultimedia/QMediaObject
/usr/include/qt5/QtMultimedia/QMediaPlayer
/usr/include/qt5/QtMultimedia/QMediaPlayerControl
/usr/include/qt5/QtMultimedia/QMediaPlaylist
/usr/include/qt5/QtMultimedia/QMediaRecorder
/usr/include/qt5/QtMultimedia/QMediaRecorderControl
/usr/include/qt5/QtMultimedia/QMediaResource
/usr/include/qt5/QtMultimedia/QMediaResourceList
/usr/include/qt5/QtMultimedia/QMediaService
/usr/include/qt5/QtMultimedia/QMediaServiceCameraInfoInterface
/usr/include/qt5/QtMultimedia/QMediaServiceDefaultDeviceInterface
/usr/include/qt5/QtMultimedia/QMediaServiceFeaturesInterface
/usr/include/qt5/QtMultimedia/QMediaServiceProviderFactoryInterface
/usr/include/qt5/QtMultimedia/QMediaServiceProviderHint
/usr/include/qt5/QtMultimedia/QMediaServiceProviderPlugin
/usr/include/qt5/QtMultimedia/QMediaServiceSupportedDevicesInterface
/usr/include/qt5/QtMultimedia/QMediaServiceSupportedFormatsInterface
/usr/include/qt5/QtMultimedia/QMediaStreamsControl
/usr/include/qt5/QtMultimedia/QMediaTimeInterval
/usr/include/qt5/QtMultimedia/QMediaTimeRange
/usr/include/qt5/QtMultimedia/QMediaVideoProbeControl
/usr/include/qt5/QtMultimedia/QMetaDataReaderControl
/usr/include/qt5/QtMultimedia/QMetaDataWriterControl
/usr/include/qt5/QtMultimedia/QMultimedia
/usr/include/qt5/QtMultimedia/QRadioData
/usr/include/qt5/QtMultimedia/QRadioDataControl
/usr/include/qt5/QtMultimedia/QRadioTuner
/usr/include/qt5/QtMultimedia/QRadioTunerControl
/usr/include/qt5/QtMultimedia/QSound
/usr/include/qt5/QtMultimedia/QSoundEffect
/usr/include/qt5/QtMultimedia/QVideoDeviceSelectorControl
/usr/include/qt5/QtMultimedia/QVideoEncoderSettings
/usr/include/qt5/QtMultimedia/QVideoEncoderSettingsControl
/usr/include/qt5/QtMultimedia/QVideoFilterRunnable
/usr/include/qt5/QtMultimedia/QVideoFrame
/usr/include/qt5/QtMultimedia/QVideoProbe
/usr/include/qt5/QtMultimedia/QVideoRendererControl
/usr/include/qt5/QtMultimedia/QVideoSurfaceFormat
/usr/include/qt5/QtMultimedia/QVideoWindowControl
/usr/include/qt5/QtMultimedia/QtMultimedia
/usr/include/qt5/QtMultimedia/QtMultimediaDepends
/usr/include/qt5/QtMultimedia/QtMultimediaVersion
/usr/include/qt5/QtMultimedia/qabstractvideobuffer.h
/usr/include/qt5/QtMultimedia/qabstractvideofilter.h
/usr/include/qt5/QtMultimedia/qabstractvideosurface.h
/usr/include/qt5/QtMultimedia/qaudio.h
/usr/include/qt5/QtMultimedia/qaudiobuffer.h
/usr/include/qt5/QtMultimedia/qaudiodecoder.h
/usr/include/qt5/QtMultimedia/qaudiodecodercontrol.h
/usr/include/qt5/QtMultimedia/qaudiodeviceinfo.h
/usr/include/qt5/QtMultimedia/qaudioencodersettingscontrol.h
/usr/include/qt5/QtMultimedia/qaudioformat.h
/usr/include/qt5/QtMultimedia/qaudioinput.h
/usr/include/qt5/QtMultimedia/qaudioinputselectorcontrol.h
/usr/include/qt5/QtMultimedia/qaudiooutput.h
/usr/include/qt5/QtMultimedia/qaudiooutputselectorcontrol.h
/usr/include/qt5/QtMultimedia/qaudioprobe.h
/usr/include/qt5/QtMultimedia/qaudiorecorder.h
/usr/include/qt5/QtMultimedia/qaudiorolecontrol.h
/usr/include/qt5/QtMultimedia/qaudiosystem.h
/usr/include/qt5/QtMultimedia/qaudiosystemplugin.h
/usr/include/qt5/QtMultimedia/qcamera.h
/usr/include/qt5/QtMultimedia/qcameracapturebufferformatcontrol.h
/usr/include/qt5/QtMultimedia/qcameracapturedestinationcontrol.h
/usr/include/qt5/QtMultimedia/qcameracontrol.h
/usr/include/qt5/QtMultimedia/qcameraexposure.h
/usr/include/qt5/QtMultimedia/qcameraexposurecontrol.h
/usr/include/qt5/QtMultimedia/qcamerafeedbackcontrol.h
/usr/include/qt5/QtMultimedia/qcameraflashcontrol.h
/usr/include/qt5/QtMultimedia/qcamerafocus.h
/usr/include/qt5/QtMultimedia/qcamerafocuscontrol.h
/usr/include/qt5/QtMultimedia/qcameraimagecapture.h
/usr/include/qt5/QtMultimedia/qcameraimagecapturecontrol.h
/usr/include/qt5/QtMultimedia/qcameraimageprocessing.h
/usr/include/qt5/QtMultimedia/qcameraimageprocessingcontrol.h
/usr/include/qt5/QtMultimedia/qcamerainfo.h
/usr/include/qt5/QtMultimedia/qcamerainfocontrol.h
/usr/include/qt5/QtMultimedia/qcameralockscontrol.h
/usr/include/qt5/QtMultimedia/qcameraviewfindersettings.h
/usr/include/qt5/QtMultimedia/qcameraviewfindersettingscontrol.h
/usr/include/qt5/QtMultimedia/qcamerazoomcontrol.h
/usr/include/qt5/QtMultimedia/qcustomaudiorolecontrol.h
/usr/include/qt5/QtMultimedia/qimageencodercontrol.h
/usr/include/qt5/QtMultimedia/qmediaaudioprobecontrol.h
/usr/include/qt5/QtMultimedia/qmediaavailabilitycontrol.h
/usr/include/qt5/QtMultimedia/qmediabindableinterface.h
/usr/include/qt5/QtMultimedia/qmediacontainercontrol.h
/usr/include/qt5/QtMultimedia/qmediacontent.h
/usr/include/qt5/QtMultimedia/qmediacontrol.h
/usr/include/qt5/QtMultimedia/qmediaencodersettings.h
/usr/include/qt5/QtMultimedia/qmediaenumdebug.h
/usr/include/qt5/QtMultimedia/qmediagaplessplaybackcontrol.h
/usr/include/qt5/QtMultimedia/qmediametadata.h
/usr/include/qt5/QtMultimedia/qmedianetworkaccesscontrol.h
/usr/include/qt5/QtMultimedia/qmediaobject.h
/usr/include/qt5/QtMultimedia/qmediaplayer.h
/usr/include/qt5/QtMultimedia/qmediaplayercontrol.h
/usr/include/qt5/QtMultimedia/qmediaplaylist.h
/usr/include/qt5/QtMultimedia/qmediarecorder.h
/usr/include/qt5/QtMultimedia/qmediarecordercontrol.h
/usr/include/qt5/QtMultimedia/qmediaresource.h
/usr/include/qt5/QtMultimedia/qmediaservice.h
/usr/include/qt5/QtMultimedia/qmediaserviceproviderplugin.h
/usr/include/qt5/QtMultimedia/qmediastreamscontrol.h
/usr/include/qt5/QtMultimedia/qmediatimerange.h
/usr/include/qt5/QtMultimedia/qmediavideoprobecontrol.h
/usr/include/qt5/QtMultimedia/qmetadatareadercontrol.h
/usr/include/qt5/QtMultimedia/qmetadatawritercontrol.h
/usr/include/qt5/QtMultimedia/qmultimedia.h
/usr/include/qt5/QtMultimedia/qradiodata.h
/usr/include/qt5/QtMultimedia/qradiodatacontrol.h
/usr/include/qt5/QtMultimedia/qradiotuner.h
/usr/include/qt5/QtMultimedia/qradiotunercontrol.h
/usr/include/qt5/QtMultimedia/qsound.h
/usr/include/qt5/QtMultimedia/qsoundeffect.h
/usr/include/qt5/QtMultimedia/qtmultimedia-config.h
/usr/include/qt5/QtMultimedia/qtmultimediadefs.h
/usr/include/qt5/QtMultimedia/qtmultimediaglobal.h
/usr/include/qt5/QtMultimedia/qtmultimediaversion.h
/usr/include/qt5/QtMultimedia/qvideodeviceselectorcontrol.h
/usr/include/qt5/QtMultimedia/qvideoencodersettingscontrol.h
/usr/include/qt5/QtMultimedia/qvideoframe.h
/usr/include/qt5/QtMultimedia/qvideoprobe.h
/usr/include/qt5/QtMultimedia/qvideorenderercontrol.h
/usr/include/qt5/QtMultimedia/qvideosurfaceformat.h
/usr/include/qt5/QtMultimedia/qvideowindowcontrol.h
/usr/include/qt5/QtMultimediaGstTools/QtMultimediaGstTools
/usr/include/qt5/QtMultimediaGstTools/QtMultimediaGstToolsDepends
/usr/include/qt5/QtMultimediaGstTools/QtMultimediaGstToolsVersion
/usr/include/qt5/QtMultimediaGstTools/qtmultimediagsttoolsversion.h
/usr/include/qt5/QtMultimediaQuick/5.12.4/QtMultimediaQuick/private/qdeclarativevideooutput_render_p.h
/usr/include/qt5/QtMultimediaQuick/5.12.4/QtMultimediaQuick/private/qdeclarativevideooutput_window_p.h
/usr/include/qt5/QtMultimediaQuick/5.12.4/QtMultimediaQuick/private/qsgvideonode_rgb_p.h
/usr/include/qt5/QtMultimediaQuick/5.12.4/QtMultimediaQuick/private/qsgvideonode_texture_p.h
/usr/include/qt5/QtMultimediaQuick/5.12.4/QtMultimediaQuick/private/qsgvideonode_yuv_p.h
/usr/include/qt5/QtMultimediaQuick/QtMultimediaQuick
/usr/include/qt5/QtMultimediaQuick/QtMultimediaQuickDepends
/usr/include/qt5/QtMultimediaQuick/QtMultimediaQuickVersion
/usr/include/qt5/QtMultimediaQuick/qtmultimediaquickversion.h
/usr/include/qt5/QtMultimediaWidgets/5.12.4/QtMultimediaWidgets/private/qpaintervideosurface_p.h
/usr/include/qt5/QtMultimediaWidgets/5.12.4/QtMultimediaWidgets/private/qvideowidget_p.h
/usr/include/qt5/QtMultimediaWidgets/QCameraViewfinder
/usr/include/qt5/QtMultimediaWidgets/QGraphicsVideoItem
/usr/include/qt5/QtMultimediaWidgets/QVideoWidget
/usr/include/qt5/QtMultimediaWidgets/QVideoWidgetControl
/usr/include/qt5/QtMultimediaWidgets/QtMultimediaWidgets
/usr/include/qt5/QtMultimediaWidgets/QtMultimediaWidgetsDepends
/usr/include/qt5/QtMultimediaWidgets/QtMultimediaWidgetsVersion
/usr/include/qt5/QtMultimediaWidgets/qcameraviewfinder.h
/usr/include/qt5/QtMultimediaWidgets/qgraphicsvideoitem.h
/usr/include/qt5/QtMultimediaWidgets/qtmultimediawidgetdefs.h
/usr/include/qt5/QtMultimediaWidgets/qtmultimediawidgetsversion.h
/usr/include/qt5/QtMultimediaWidgets/qvideowidget.h
/usr/include/qt5/QtMultimediaWidgets/qvideowidgetcontrol.h
/usr/lib64/cmake/Qt5Multimedia/Qt5MultimediaConfig.cmake
/usr/lib64/cmake/Qt5Multimedia/Qt5MultimediaConfigVersion.cmake
/usr/lib64/cmake/Qt5Multimedia/Qt5Multimedia_CameraBinServicePlugin.cmake
/usr/lib64/cmake/Qt5Multimedia/Qt5Multimedia_QGstreamerAudioDecoderServicePlugin.cmake
/usr/lib64/cmake/Qt5Multimedia/Qt5Multimedia_QGstreamerCaptureServicePlugin.cmake
/usr/lib64/cmake/Qt5Multimedia/Qt5Multimedia_QGstreamerPlayerServicePlugin.cmake
/usr/lib64/cmake/Qt5Multimedia/Qt5Multimedia_QM3uPlaylistPlugin.cmake
/usr/lib64/cmake/Qt5Multimedia/Qt5Multimedia_QPulseAudioPlugin.cmake
/usr/lib64/cmake/Qt5MultimediaWidgets/Qt5MultimediaWidgetsConfig.cmake
/usr/lib64/cmake/Qt5MultimediaWidgets/Qt5MultimediaWidgetsConfigVersion.cmake
/usr/lib64/libQt5Multimedia.prl
/usr/lib64/libQt5Multimedia.so
/usr/lib64/libQt5MultimediaGstTools.prl
/usr/lib64/libQt5MultimediaGstTools.so
/usr/lib64/libQt5MultimediaQuick.prl
/usr/lib64/libQt5MultimediaQuick.so
/usr/lib64/libQt5MultimediaWidgets.prl
/usr/lib64/libQt5MultimediaWidgets.so
/usr/lib64/pkgconfig/Qt5Multimedia.pc
/usr/lib64/pkgconfig/Qt5MultimediaWidgets.pc
/usr/lib64/qt5/mkspecs/modules/qt_lib_multimedia.pri
/usr/lib64/qt5/mkspecs/modules/qt_lib_multimedia_private.pri
/usr/lib64/qt5/mkspecs/modules/qt_lib_multimediagsttools_private.pri
/usr/lib64/qt5/mkspecs/modules/qt_lib_multimediawidgets.pri
/usr/lib64/qt5/mkspecs/modules/qt_lib_multimediawidgets_private.pri
/usr/lib64/qt5/mkspecs/modules/qt_lib_qtmultimediaquicktools_private.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libQt5Multimedia.so.5
/usr/lib64/libQt5Multimedia.so.5.12
/usr/lib64/libQt5Multimedia.so.5.12.4
/usr/lib64/libQt5MultimediaGstTools.so.5
/usr/lib64/libQt5MultimediaGstTools.so.5.12
/usr/lib64/libQt5MultimediaGstTools.so.5.12.4
/usr/lib64/libQt5MultimediaQuick.so.5
/usr/lib64/libQt5MultimediaQuick.so.5.12
/usr/lib64/libQt5MultimediaQuick.so.5.12.4
/usr/lib64/libQt5MultimediaWidgets.so.5
/usr/lib64/libQt5MultimediaWidgets.so.5.12
/usr/lib64/libQt5MultimediaWidgets.so.5.12.4
/usr/lib64/qt5/plugins/audio/libqtmedia_pulse.so
/usr/lib64/qt5/plugins/mediaservice/libgstaudiodecoder.so
/usr/lib64/qt5/plugins/mediaservice/libgstcamerabin.so
/usr/lib64/qt5/plugins/mediaservice/libgstmediacapture.so
/usr/lib64/qt5/plugins/mediaservice/libgstmediaplayer.so
/usr/lib64/qt5/plugins/playlistformats/libqtmultimedia_m3u.so
/usr/lib64/qt5/qml/QtAudioEngine/libdeclarative_audioengine.so
/usr/lib64/qt5/qml/QtAudioEngine/plugins.qmltypes
/usr/lib64/qt5/qml/QtAudioEngine/qmldir
/usr/lib64/qt5/qml/QtMultimedia/Video.qml
/usr/lib64/qt5/qml/QtMultimedia/libdeclarative_multimedia.so
/usr/lib64/qt5/qml/QtMultimedia/plugins.qmltypes
/usr/lib64/qt5/qml/QtMultimedia/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qtmultimedia/LICENSE.FDL
/usr/share/package-licenses/qtmultimedia/LICENSE.GPL2
/usr/share/package-licenses/qtmultimedia/LICENSE.GPL3
/usr/share/package-licenses/qtmultimedia/LICENSE.GPL3-EXCEPT
/usr/share/package-licenses/qtmultimedia/LICENSE.LGPL3
/usr/share/package-licenses/qtmultimedia/examples_multimedia_spectrum_3rdparty_fftreal_license.txt
