import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-oca-purchase-workflow",
    description="Meta package for oca-purchase-workflow Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-partner_supplierinfo_smartbutton',
        'odoo14-addon-procurement_batch_generator',
        'odoo14-addon-procurement_purchase_no_grouping',
        'odoo14-addon-product_form_purchase_link',
        'odoo14-addon-product_supplier_code_purchase',
        'odoo14-addon-purchase_advance_payment',
        'odoo14-addon-purchase_allowed_product',
        'odoo14-addon-purchase_analytic_global',
        'odoo14-addon-purchase_blanket_order',
        'odoo14-addon-purchase_cancel_confirm',
        'odoo14-addon-purchase_cancel_reason',
        'odoo14-addon-purchase_commercial_partner',
        'odoo14-addon-purchase_default_terms_conditions',
        'odoo14-addon-purchase_delivery_split_date',
        'odoo14-addon-purchase_deposit',
        'odoo14-addon-purchase_discount',
        'odoo14-addon-purchase_exception',
        'odoo14-addon-purchase_fop_shipping',
        'odoo14-addon-purchase_force_invoiced',
        'odoo14-addon-purchase_invoice_method',
        'odoo14-addon-purchase_invoice_plan',
        'odoo14-addon-purchase_invoice_plan_deposit',
        'odoo14-addon-purchase_invoice_plan_retention',
        'odoo14-addon-purchase_isolated_rfq',
        'odoo14-addon-purchase_last_price_info',
        'odoo14-addon-purchase_location_by_line',
        'odoo14-addon-purchase_lot',
        'odoo14-addon-purchase_manual_currency',
        'odoo14-addon-purchase_manual_delivery',
        'odoo14-addon-purchase_mass_mail',
        'odoo14-addon-purchase_minimum_amount',
        'odoo14-addon-purchase_open_qty',
        'odoo14-addon-purchase_order_approval_block',
        'odoo14-addon-purchase_order_approved',
        'odoo14-addon-purchase_order_archive',
        'odoo14-addon-purchase_order_general_discount',
        'odoo14-addon-purchase_order_line_deep_sort',
        'odoo14-addon-purchase_order_line_description_picking',
        'odoo14-addon-purchase_order_line_image',
        'odoo14-addon-purchase_order_line_invoicing',
        'odoo14-addon-purchase_order_line_menu',
        'odoo14-addon-purchase_order_line_packaging_qty',
        'odoo14-addon-purchase_order_line_price_history',
        'odoo14-addon-purchase_order_line_price_history_discount',
        'odoo14-addon-purchase_order_line_sequence',
        'odoo14-addon-purchase_order_line_stock_available',
        'odoo14-addon-purchase_order_partner_manual_rank',
        'odoo14-addon-purchase_order_payment_term_report',
        'odoo14-addon-purchase_order_price_recalculation',
        'odoo14-addon-purchase_order_product_attachment_mgmt',
        'odoo14-addon-purchase_order_qty_change_no_recompute',
        'odoo14-addon-purchase_order_secondary_unit',
        'odoo14-addon-purchase_order_shipping_date',
        'odoo14-addon-purchase_order_type',
        'odoo14-addon-purchase_order_type_dashboard',
        'odoo14-addon-purchase_order_uninvoiced_amount',
        'odoo14-addon-purchase_order_vendor_product',
        'odoo14-addon-purchase_order_weight_volume',
        'odoo14-addon-purchase_partner_approval',
        'odoo14-addon-purchase_partner_incoterm',
        'odoo14-addon-purchase_picking_state',
        'odoo14-addon-purchase_product_usage',
        'odoo14-addon-purchase_propagate_qty',
        'odoo14-addon-purchase_quick',
        'odoo14-addon-purchase_reception_notify',
        'odoo14-addon-purchase_reception_status',
        'odoo14-addon-purchase_report_menu_move',
        'odoo14-addon-purchase_representative',
        'odoo14-addon-purchase_request',
        'odoo14-addon-purchase_request_cancel_confirm',
        'odoo14-addon-purchase_request_department',
        'odoo14-addon-purchase_request_exception',
        'odoo14-addon-purchase_request_substate',
        'odoo14-addon-purchase_request_tier_validation',
        'odoo14-addon-purchase_request_to_requisition',
        'odoo14-addon-purchase_request_type',
        'odoo14-addon-purchase_requisition_auto_rfq',
        'odoo14-addon-purchase_requisition_tier_validation',
        'odoo14-addon-purchase_rfq_number',
        'odoo14-addon-purchase_security',
        'odoo14-addon-purchase_stock_price_unit_sync',
        'odoo14-addon-purchase_stock_secondary_unit',
        'odoo14-addon-purchase_stock_tier_validation',
        'odoo14-addon-purchase_stock_vendor_bill_breakdown',
        'odoo14-addon-purchase_substate',
        'odoo14-addon-purchase_supplierinfo_product_breakdown',
        'odoo14-addon-purchase_tag',
        'odoo14-addon-purchase_tier_validation',
        'odoo14-addon-purchase_triple_discount',
        'odoo14-addon-purchase_vendor_bill_breakdown',
        'odoo14-addon-purchase_work_acceptance',
        'odoo14-addon-purchase_work_acceptance_evaluation',
        'odoo14-addon-purchase_work_acceptance_invoice_plan',
        'odoo14-addon-purchase_work_acceptance_late_fines',
        'odoo14-addon-purchase_work_acceptance_tier_validation',
        'odoo14-addon-sale_purchase_force_vendor',
        'odoo14-addon-subcontracted_service',
        'odoo14-addon-vendor_transport_lead_time',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 14.0',
    ]
)
