Summary:	Simple image viewer for GNUstep
Summary(pl):	Prosta przegl±darka obrazków dla ¶rodowiska GNUstep
Name:		ImageViewer
Version:	0.6.3
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://www.nice.ch/~phip/%{name}-%{version}.tar.gz
# Source0-md5:	89dc35241be2e4c60c80d51adb110c65
Patch0:		%{name}-pass-arguments.patch
URL:		http://www.nice.ch/~phip/softcorner.html#img
BuildRequires:	gnustep-gui-devel >= 0.8.7
Requires:	gnustep-gui >= 0.8.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/%{_lib}/GNUstep

%define		libcombo	gnu-gnu-gnu
%define		gsos		linux-gnu
%ifarch %{ix86}
%define		gscpu		ix86
%else
# also s/alpha.*/alpha/, but we use only "alpha" arch for now
%define		gscpu		%(echo %{_target_cpu} | sed -e 's/amd64/x86_64/;s/ppc/powerpc/')
%endif

%description
This is ImageViewer, a simple image viewer application for GNUstep.

%description -l pl
To jest ImageViewer - prosta przegl±darka obrazków dla ¶rodowiska
GNUstep.

%prep
%setup -q
%patch0 -p1

%build
. %{_prefix}/System/Library/Makefiles/GNUstep.sh
%{__make} \
	OPTFLAG="%{rpmcflags}" \
	messages=yes

%install
rm -rf $RPM_BUILD_ROOT
. %{_prefix}/System/Library/Makefiles/GNUstep.sh

%{__make} install \
	GNUSTEP_INSTALLATION_DIR=$RPM_BUILD_ROOT%{_prefix}/System

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%dir %{_prefix}/System/Applications/ImageViewer.app
%attr(755,root,root) %{_prefix}/System/Applications/ImageViewer.app/ImageViewer
%dir %{_prefix}/System/Applications/ImageViewer.app/Resources
%{_prefix}/System/Applications/ImageViewer.app/Resources/*.desktop
%{_prefix}/System/Applications/ImageViewer.app/Resources/*.plist
%{_prefix}/System/Applications/ImageViewer.app/Resources/*.tiff
%{_prefix}/System/Applications/ImageViewer.app/Resources/English.lproj
%lang(fr) %{_prefix}/System/Applications/ImageViewer.app/Resources/French.lproj
%lang(de) %{_prefix}/System/Applications/ImageViewer.app/Resources/German.lproj
%lang(hu) %{_prefix}/System/Applications/ImageViewer.app/Resources/Hungarian.lproj
%dir %{_prefix}/System/Applications/ImageViewer.app/%{gscpu}
%dir %{_prefix}/System/Applications/ImageViewer.app/%{gscpu}/%{gsos}
%dir %{_prefix}/System/Applications/ImageViewer.app/%{gscpu}/%{gsos}/%{libcombo}
%attr(755,root,root) %{_prefix}/System/Applications/ImageViewer.app/%{gscpu}/%{gsos}/%{libcombo}/ImageViewer
%{_prefix}/System/Applications/ImageViewer.app/%{gscpu}/%{gsos}/%{libcombo}/*.openapp
