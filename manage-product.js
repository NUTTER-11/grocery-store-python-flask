var productModal = $("#productModal");     //this has code for both show list delete an element and add an element 3 api are called here 
    $(function () {

        //JSON data by API call   for getting all the products displayed
        $.get(productListApiUrl, function (response) {
            if(response) {
                var table = '';
                $.each(response, function(index, product) {
                    table += '<tr data-id="'+ product.product_id +'" data-name="'+ product.name +'" data-unit="'+ product.uom_id +'" data-price="'+ product.price_per_unit +'">' +
                        '<td>'+ product.name +'</td>'+
                        '<td>'+ product.uom_name +'</td>'+
                        '<td>'+ product.price_per_unit +'</td>'+
                        '<td><span class="btn btn-xs btn-danger delete-product">Delete</span></td></tr>';
                });
                $("table").find('tbody').empty().html(table);
            }
        });
    });

    // Save Product
    $("#saveProduct").on("click", function () {
        // If we found id value in form then update product detail
        var data = $("#productForm").serializeArray();
        var requestPayload = {
            product_name: null,//pre enterted values
            uom_id: null,//pre enterted values
            price_per_unit: null//pre enterted values
        };
        for (var i=0;i<data.length;++i) {
            var element = data[i];
            switch(element.name) {
                case 'name':
                    requestPayload.product_name = element.value;// new enterted values
                    break;
                case 'uoms':
                    requestPayload.uom_id = element.value;//new enterted values
                    break;
                case 'price':
                    requestPayload.price_per_unit = element.value;// new enterted values
                    break;
            }
        }
        callApi("POST", productSaveApiUrl, {
            'data': JSON.stringify(requestPayload)
        });
    });

    $(document).on("click", ".delete-product", function (){
        var tr = $(this).closest('tr');//to know what roe=w needs to be deleted
        var data = {
            product_id : tr.data('id')
        };
        var isDelete = confirm("Are you sure to delete "+ tr.data('name') +" item?"); //popupmessage
        if (isDelete) {
            callApi("POST", productDeleteApiUrl, data);
        }
    });
// switch case toggel used for add button 
    productModal.on('hide.bs.modal', function(){// when save or cancel is pressed
        $("#id").val('0');
        $("#name, #unit, #price").val('');
        productModal.find('.modal-title').text('Add New Product');
    });

    productModal.on('show.bs.modal', function(){     //   when the add button is pressed
        //JSON data by API call
        $.get(uomListApiUrl, function (response) {  //uom is called here 
            if(response) {
                var options = '<option value="">--Select--</option>';
                $.each(response, function(index, uom) {
                    options += '<option value="'+ uom.uom_id +'">'+ uom.uom_name +'</option>';
                });
                $("#uoms").empty().html(options);
            }
        });
    });


    