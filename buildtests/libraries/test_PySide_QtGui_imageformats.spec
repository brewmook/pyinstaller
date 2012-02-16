# -*- mode: python -*-

__testname__ = 'test_PySide_QtGui_imageformats'
__sample_image__ = 'tinysample.tiff'

a = Analysis([__testname__ + '.py'])
pyz = PYZ(a.pure)

TOC_custom = [(__sample_image__,__sample_image__,'DATA')]

exe = EXE(pyz,
          a.scripts,
          exclude_binaries=1,
          name=os.path.join('build',
                            'pyi.' + sys.platform,
                            __testname__,
                            __testname__ + '.exe'),
          debug=True,
          strip=None,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               TOC_custom,
               strip=None,
               upx=True,
               name=os.path.join('dist', __testname__))
