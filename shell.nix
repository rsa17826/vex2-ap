{
  pkgs ? import <nixpkgs> { },
}:

pkgs.mkShell {
  buildInputs = with pkgs; [
    python313
    git
    gnumake
    gcc

    # Kivy / Window dependencies
    stdenv.cc.cc.lib # Provides libstdc++.so.6
    libGL # Provides libGL.so.1
    libX11
    libXext
    libXrender
    libXrandr
    libXcursor
    libXinerama
    libXi
    libXfixes
  ];

  # This environment variable tells pre-compiled binaries where to find the graphics drivers
  LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath (
    with pkgs;
    [
      stdenv.cc.cc.lib
      libGL
      libX11
    ]
  );
  shellHook = ''
    source /home/nyix/projects/Archipelago/.venv/bin/activate
  '';
}
