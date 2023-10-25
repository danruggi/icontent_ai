<?php

// Will be called with a get
$art_id = $_GET['id'];
$art_lan = $_GET['lan'];


$docroot=$_SERVER['DOCUMENT_ROOT'];

// Read the file line by line into an array
$art_json = $docroot."/fe/articles/".$art_lan."/".$art_id.".json";
if (file_exists($art_json)) {
    $lines = file($art_json, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
    // Proceed with reading the file
} else {
    error_plain("Article not exists");
    // You can return an error code or handle the error in the way you prefer.
}

// Loop through each line
foreach ($lines as $line) {
    // Parse each line as a JSON object
    $data = json_decode($line, true);

    if ($data !== null) {
    	if ($art_id != $data['art_id']) continue;
        // Process the JSON data here
        $title = $data['title'];
        $description = $data['desc'];
        // Access other fields as needed

        // You can also perform additional processing on each JSON object
    }
}

?>

<!DOCTYPE html>
<html lang='<?=$art_lan?>'>

<body>
	<div class="page-wrapper-loader relative">
		<div class="flex-centered abs-centered">
			<div class="logo"> 
				<h1 class="m0">xxx</h1>
			</div>
			<img alt="deskydoo-logo-icon" src="<?=$cdn_img?>/assets/be/logo.gif" width="128" height="128" class="m0a mt3">
		</div>
	</div>

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

		<?php
			$section_colors = ['pink', 'azul', 'green', 'gray', 'red', ''];
			$i=0;
			foreach ($data['par'] as $section_text) {
				if ($i < sizeof($data['images'])){
					$section_class = $section_colors[array_rand($section_colors)];
					$st = str_replace('.', '.</p><p>', $section_text);
					$section_img = $data['images'][$i];
					$section_img = '/fe/articles/imgs/'.$art_id.'/'.basename($section_img);
					$section_has_image = true;
				} else {
					$section_class = "";
					$st = $section_text;
					$section_img = "";
					$section_has_image = false;
				}
				if (strpos($st, 'SEO') !== false) { continue; }
				if (strpos($st, 'Keyword') !== false) {continue; }
				$i++;
		?>
				<!-- Article Section <?=$i?> -->
				<section  class="<?=$section_class?>">
					<?php if ($section_has_image) { ?>

						<div class="sides">
							<div class="gap-controlled inview-animation">
								<?php if (($i % 2) == 0) { ?>
									<div class="img-wrapper left" style="margin-bottom: 1rem; margin-top: 1rem;">
										<div class="flex-centered">
											<img title="Cleaning procedures optimization" alt="cleaning process, on checkout, room is setup as dirty, reception always informed about cleaning status" src="<?=$section_img?>" width="728" height="728">
										</div>
									</div>
									<div class="text-wrapper ml2">
										<p><?=$st?></p>
									</div>
								<?php } else { ?>
									<div class="text-wrapper left">
										<p><?=$st?></p>
									</div>
									<div class="img-wrapper" style="margin-bottom: 1rem; margin-top: 1rem;">
										<div class="flex-centered">
											<img title="Cleaning procedures optimization" alt="cleaning process, on checkout, room is setup as dirty, reception always informed about cleaning status" src="<?=$section_img?>" width="728" height="728" style=>
										</div>
									</div>
								<?php } ?>
							</div>
						</div>
					<?php } else { ?>
						<div class="grid-container grid-1col">
							<div class="flex-container" style="margin: 1rem auto; width: 60%;">
								<div class="ta-c">
									<p><?=$st?></p>
								</div>
							</div>
						</div>
					<?php } ?>
					<div class="flex-container centered font-comf">
						<div class="">
						</div>
					</div>
				</section>
		<?php  	} 	?>

	</div>

</body>

</html>