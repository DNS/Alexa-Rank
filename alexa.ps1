

function Write-Alexa {
    foreach ($i in $args) {
        $ret = get-alexa $i
        if (-not $ret) {
            Write-Host $i 'not ranked'
            Continue
        }
        $global_rank, $local_rank, $local_coutry = $ret
        Write-Host $i 'Global rank:' $global_rank
        Write-Host $i ${local_coutry} 'rank:' $local_rank
    }
}

function Get-Alexa {
    $url = 'http://data.alexa.com/data?cli=10&url='+$i
    [xml] $r = Invoke-RestMethod -Uri $url -TimeoutSec 30
    if (-not $r.ALEXA.SD.POPULARITY.TEXT) {
        return 0
    }
    $global_rank = $r.ALEXA.SD.POPULARITY.TEXT
    $local_rank = $r.ALEXA.SD.COUNTRY.RANK
    $local_coutry = $r.ALEXA.SD.COUNTRY.NAME
    return $global_rank, $local_rank, $local_coutry
}


Write-Alexa 'WWst994ctc03.com' 'zalora.com'





<#

<ALEXA VER="0.9" URL="matahari.com/" HOME="0" AID="=" IDN="matahari.com/">
    <SD>
        <POPULARITY URL="matahari.com/" TEXT="258160" SOURCE="panel"/>
        <REACH RANK="269155"/>
        <RANK DELTA="+57275"/>
        <COUNTRY CODE="ID" NAME="Indonesia" RANK="5048"/>
    </SD>
</ALEXA>

#>


