window.onload = function () {
	var so_r = document.getElementById('so_r');
	var cu_r = document.getElementById('cu_r');
	var po_r = document.getElementById('po_r');
	var ec_r = document.getElementById('ec_r');
	var en_r = document.getElementById('en_r');
	var fr_r = document.getElementById('fr_r');
	var so = document.getElementById('SO');
	var cu = document.getElementById('CU');
	var po = document.getElementById('PO');
	var ec = document.getElementById('EC');
	var en = document.getElementById('EN');
	var fr = document.getElementById('FR');

	so_r.onclick = function () {
		so.style.display = 'flex';
		cu.style.display = 'none';
		po.style.display = 'none';
		ec.style.display = 'none';
		en.style.display = 'none';
		fr.style.display = 'none';
	}

	cu_r.onclick = function () {
		so.style.display = 'none';
		cu.style.display = 'flex';
		po.style.display = 'none';
		ec.style.display = 'none';
		en.style.display = 'none';
		fr.style.display = 'none';
	}

	po_r.onclick = function () {
		so.style.display = 'none';
		cu.style.display = 'none';
		po.style.display = 'flex';
		ec.style.display = 'none';
		en.style.display = 'none';
		fr.style.display = 'none';
	}

	ec_r.onclick = function () {
		so.style.display = 'none';
		cu.style.display = 'none';
		po.style.display = 'none';
		ec.style.display = 'flex';
		en.style.display = 'none';
		fr.style.display = 'none';
	}

	en_r.onclick = function () {
		so.style.display = 'none';
		cu.style.display = 'none';
		po.style.display = 'none';
		ec.style.display = 'none';
		en.style.display = 'flex';
		fr.style.display = 'none';
	}

	fr_r.onclick = function () {
		so.style.display = 'none';
		cu.style.display = 'none';
		po.style.display = 'none';
		ec.style.display = 'none';
		en.style.display = 'none';
		fr.style.display = 'flex';
	}
}

