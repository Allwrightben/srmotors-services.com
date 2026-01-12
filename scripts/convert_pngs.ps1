Add-Type -AssemblyName System.Drawing
$imgDir = Join-Path $PSScriptRoot '..\images'
$pngs = Get-ChildItem -Path $imgDir -File | Where-Object { $_.Extension -in '.png', '.PNG' }
if ($pngs.Count -eq 0) { Write-Host 'No PNGs found.'; exit }
$codec = [System.Drawing.Imaging.ImageCodecInfo]::GetImageEncoders() | Where-Object { $_.MimeType -eq 'image/jpeg' }
$params = New-Object System.Drawing.Imaging.EncoderParameters(1)
$params.Param[0] = New-Object System.Drawing.Imaging.EncoderParameter([System.Drawing.Imaging.Encoder]::Quality, 85L)
foreach ($f in $pngs) {
  $img = [System.Drawing.Image]::FromFile($f.FullName)
  $bmp = New-Object System.Drawing.Bitmap $img.Width, $img.Height
  $g = [System.Drawing.Graphics]::FromImage($bmp)
  $g.Clear([System.Drawing.Color]::White)
  $g.DrawImage($img, 0,0, $img.Width, $img.Height)
  $g.Dispose()
  $dst = Join-Path $f.DirectoryName ($f.BaseName + '.jpg')
  $bmp.Save($dst, $codec, $params)
  $bmp.Dispose(); $img.Dispose()
  Remove-Item $f.FullName
  Write-Host "Converted $($f.Name) -> $([System.IO.Path]::GetFileName($dst))"
}