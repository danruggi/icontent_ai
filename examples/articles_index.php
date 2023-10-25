<?php

// This is just an example, you need to edit it to make it work

$docroot=$_SERVER['DOCUMENT_ROOT'];
$avl_lng = array('en', 'it', 'es');

$art_lan = 'en';

// Here you need the relative path og your articles folder
$art_json = $docroot."/fe/articles/".$art_lan."_arts.json";
if (file_exists($art_json)) {
    $lines = file($art_json, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
    // Proceed with reading the file
} else {
    error_plain("No Articles availables");
    // You can return an error code or handle the error in the way you prefer.
}

$title = "Blog";
$description = "Latest news about hospitality industry";

// Main Config
// Temlplate vars
// $title = _("DeskyDoo housekeeping management");
// $description = _("Deskydoo helps you administer and manage the cleaning procedures in your property. If you have one or more maid, a cleaning staff, a external team, there is an ad-hoc interface to organize the daily duties, keep reception updated, and to create reports about what employees did");
// $description = _("Same as more expensive softwares, but cheaper, faster, with more functionalities, and better coded");

$css_slow_arr = array('fonts_all.css', 'buttons.css', 'ul.css', 'colors.css', 'pages-headers.css');

// echo gettext('ciao');
?>

<!DOCTYPE html>
<html lang='<?=$art_lan?>'>
<head>
	<title><?=$title?></title>
<body>

	<!-- ***** FULL PAGE HERE -->
	<div class="full-container">

		<!-- HEADER -->
		<header class="middle-write">
			<div class="title-wrapper">
				<div class="flex-centered m2">
					<h1><?=$title?></h1>
					<span><?=$description?></span>
				</div>
			</div>
			
		</header>
		<style>
			section.cards a {
				color: white;
			}
			section.cards a:hover {
				color: orange;
			}
			section.cards .card {
				background: #202020;
				border-radius: 4px;
				padding: 1rem;
			}
		</style>
		<section class="cards flex-container">
			<div class="margined-container">
				<div class="grid-container grid-2col m2">
					<?php 
						$tot_arts = 0;
						for ($i = count($lines) - 1; $i >= 0; $i--) {
							if ($tot_arts >= 10) {
								break;
							}
						    $line = $lines[$i];
						    $data = json_decode($line, true);

						    if ($data !== null) {
						        // Process the JSON data here
						        $title = $data['title'];
						        $desc = $data['desc'];
						        $excert = $data['excert'];
						        $post_num = $data['post_num'];
						        $img = '/fe/articles/imgs/'.$post_num."/".basename($data['img']);
						        $ts = $data['ts'];
						        $datetime = date('d M Y, H:i', strtotime(substr($ts, 0, 8) . ' ' . substr($ts, 9, 4)));
						    }

					?>
					<a href="/fe/articles/articles_load?id=<?=$post_num?>&lan=<?=$art_lan?>">
						<div class="card full-container azul">
							<div class="img-wrapper" style="margin:unset">
								<img title="Blog Image" alt="Image about <?$title?>" src="<?=$img?>" width="480" height="320" style='width: 90%;'>
							</div>
							<div class="ta-c font-dosis">
								<h3><?=$title?></h3>
							</div>
							<div class="ta-c font-dosis">
								<h5><?=$desc?></h5>
							</div>
							<div class="ta-c">
								<p>
									<em><?=$excert?></em>	
								</p>
							</div>
							<div class="grid-container smaller" style="font-size:0.6em">
								<p class="smaller">
									by Daniele Rugginenti
								</p>
								<p class="smaller ta-r">
									<em><?=$datetime?></em>
								</p>
							</div>
						</div>
					</a>	
					<?php } ?>
				</div>
			</div>
		</section>
	</div>

</body>
</html>